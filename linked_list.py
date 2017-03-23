from linked_list_node import LinkedListNode

# Doubly linked list class that will contain the keys and values
# in a given "bucket" of our hashmap

class LinkedList:
    # list starts as empty
    def __init__(self):
        self.head = LinkedListNode()
        self.tail = LinkedListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    # append a new node to the list (this takes O(1) time)
    def append(self, key, value):
        new_node = LinkedListNode(key, value)

        self.tail.prev.next = new_node
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        self.tail.prev = new_node

        return new_node

    # find the item with the given key and update it (this takes O(n) time)
    def update(self, key, value):
        current_node = self.head.next

        while current_node != self.tail:
            if current_node.key == key:
                current_node.value = value
                return current_node.value

            current_node = current_node.next

        return None

    # find the item with the given key and remove it (this takes O(n) time)
    def remove(self, key):
        current_node = self.head.next

        while current_node != self.tail:
            if current_node.key == key:
                current_node.remove()
                return current_node.value

            current_node = current_node.next

        return None

    # find the item with the given key and return its corresponding value
    # (this takes O(n) time)
    def get(self, key):
        current_node = self.head.next

        while current_node != self.tail:
            if current_node.key == key:
                return current_node.value

            current_node = current_node.next

        return None

    # check if list is empty
    def is_empty(self):
        return self.head.next == self.tail

    # check if given key included in list
    def is_included(self, key):
        value = self.get(key)
        return value is not None

    # return tuples of all the key, value pairs
    def items(self):
        return self.get_subset()

    # return a list of all keys
    def keys(self):
        return self.get_subset("keys")

    # return a list of all values
    def values(self):
        return self.get_subset("values")

    # helper method to get all keys or values
    def get_subset(self, subset = "items"):
        items = []
        current_node = self.head.next

        while current_node != self.tail:
            if subset == "values":
                items.append(current_node.value)
            elif subset == "keys":
                items.append(current_node.key)
            else:
                pair = (current_node.key, current_node.value)
                items.append(pair)

            current_node = current_node.next

        return items
