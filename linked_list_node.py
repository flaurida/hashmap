# Linked list node class that holds individual links for linked list
# Each link contains references to its key and value as well as
# to the next and previous links in the list
# includes a method for link to remove itself from list
# (note this is an O(1) operation)

class LinkedListNode:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def remove(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        self.next = None
        self.prev = None

        return self
