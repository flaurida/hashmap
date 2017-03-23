import hashlib
from linked_list import LinkedList

# Hashmap class constructed using a list of "buckets" where
# each bucket is a linked list of nodes that contain the a key/value pair
# By keeping the number of buckets at least as large as the total
# number of key/value pairs in the hashmap, this gives amortized
# O(1) lookup time
# (Note: the index of an key's associated "bucket" is determined by
# the output of a hash function % the total number of buckets)

class HashMap:
    # initialize empty hash map with desired number of buckets
    def __init__(self, num_buckets = 8):
        self.store = self.initialize_store(num_buckets)
        self.count = 0

    # bracket method to get the value of a given key
    # raises error if key not included
    def __getitem__(self, key):
        value = self.get_value(key)

        if value is not None:
            return value

        raise KeyError("That key is not included")

    # bracket method to get the value of a given key
    # returns default value if key not included
    def get(self, key, default_value = None):
        value = self.get_value(key)

        if value is not None:
            return value

        return default_value

    # helper method to get the value associated with key
    def get_value(self, key):
        bucket = self.bucket(key)
        return bucket.get(key)

    # []= method that adds or updates value for a given key
    # also increases the number of buckets if the number of key/value pairs
    # is larger than the number of buckets
    def __setitem__(self, key, value):
        bucket = self.bucket(key)

        if bucket.is_included(key):
            bucket.update(key, value)
        else:
            bucket.append(key, value)
            self.count += 1

        if self.count > self.num_buckets():
            self.resize()

        return value

    # delete a given key from the hashmap
    def delete(self, key):
        value = self.bucket(key).remove(key)

        if value is not None:
            self.count -= 1
            if self.count < self.num_buckets() / 4:
                self.resize(False)

        return value

    # boolean method to see if hashmap has key
    def has_key(self, key):
        bucket = self.bucket(key)
        return bucket.is_included(key)

    # method to add another hashmap's key/value pairs to current hashmap
    def update(self, other_hash_map):
        for key, value in other_hash_map.items():
            self[key] = value

        return self

    # create a new list of buckets that is larger or smaller than existing list
    # (depending on whether number of buckets is too high or too low)
    # then copy over key/value pairs into their new associated buckets
    # Note that number of buckets never goes below 8 to avoid tons of
    # growing/shrinking when number of key/value pairs is very low
    def resize(self, grow = True):
        new_num_buckets = self.num_buckets() * 2 if grow else self.num_buckets() / 2

        if new_num_buckets < 8:
            return

        old_store = self.store
        self.store = self.initialize_store(new_num_buckets)
        self.count = 0

        for bucket in old_store:
            item = bucket.head.next

            while item != bucket.tail:
                self[item.key] = item.value
                item = item.next

        return self

    # so that len(hashmap) works as in Python
    def __len__(self):
        return self.count

    # boolean method to see if hashmap is empty
    def is_empty(self):
        return self.count == 0

    # how many buckets?
    def num_buckets(self):
        return len(self.store)

    # use a hash function % the total number of buckets
    # to find associated bucket for given key
    def bucket(self, key):
        bucket_idx = hash(key) % self.num_buckets()
        return self.store[bucket_idx]

    # create a new list of num_buckets linked lists
    # Note buckets is at minimum 8 to avoid growing/shrinking
    # frequently when number of key/value pairs is very small
    def initialize_store(self, num_buckets):
        new_store = []
        if num_buckets < 8:
            num_buckets = 8

        while len(new_store) < num_buckets:
            new_store.append(LinkedList())

        return new_store

    # return list of (key, value) for all key value pairs
    def items(self):
        return self.get_subset()

    # return list of all keys in hashmap
    def keys(self):
        return self.get_subset("keys")

    # return list of all values in hashmap
    def values(self):
        return self.get_subset("values")

    # helper method to grab the keys, values, or both from hashmap
    def get_subset(self, subset = "items"):
        items = []

        for bucket in self.store:
            if subset == "keys":
                items += bucket.keys()
            elif subset == "values":
                items += bucket.values()
            else:
                items += bucket.items()

        return items

    # method that prints out hashmap the way Python does
    def __str__(self):
        pretty_items = []

        for pair in self.items():
            pretty_pair  = ": ".join(self.format_pair(pair))
            pretty_items.append(pretty_pair)

        return "{" + ", ".join(pretty_items) + "}"

    # helper method include single quotes around keys/values that are strings
    def pretty_string(self, string):
        return "'%s'" % string

    # format each key/value pair for printing
    def format_pair(self, pair):
        pretty_pair = ()

        for item in pair:
            if isinstance(item, basestring):
                pretty_pair += (self.pretty_string(item), )
            else:
                pretty_pair += (str(item), )

        return pretty_pair
