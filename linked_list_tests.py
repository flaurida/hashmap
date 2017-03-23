import unittest
from linked_list import LinkedList

# testing suite for basic operations in linked list class
# (create, insert, remove, update)

class LinkedListTests(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def tearDown(self):
        self.linked_list = None

    # test creation of empty linked list
    def test_create_linked_list(self):
        self.assertTrue(self.linked_list.is_empty())

    # test appending different key value pairs to linked list
    def test_append_to_linked_list(self):
        self.linked_list.append("test", "testing")
        self.assertEqual("testing", self.linked_list.get("test"))
        self.assertTrue(self.linked_list.is_included("test"))

        self.assertFalse(self.linked_list.is_included("another test"))
        self.linked_list.append("another test", "testing!")
        self.assertEqual("testing!", self.linked_list.get("another test"))
        self.assertTrue(self.linked_list.is_included("another test"))

    # test that linked list is empty after appending and then
    # removing a node
    def test_remove_from_linked_list(self):
        node = self.linked_list.append("test", "testing")
        self.linked_list.remove("test")
        self.assertTrue(self.linked_list.is_empty())

    # test that changing the associated value of a node with
    # a given key works
    def test_update_value_in_linked_list(self):
        self.linked_list.append("test", "testing")
        self.linked_list.update("test", "testing123")
        self.assertEqual("testing123", self.linked_list.get("test"))

    # test that returning all key value pairs in linked list works as expected
    def test_get_all_items_in_linked_list(self):
        self.linked_list.append("test", "testing")
        self.linked_list.append("testing!", "testing123!")

        self.assertEqual([('test', 'testing'), ('testing!', 'testing123!')], self.linked_list.items())
        self.assertEqual(['test', 'testing!'], self.linked_list.keys())
        self.assertEqual(['testing', 'testing123!'], self.linked_list.values())

if __name__ == '__main__':
    unittest.main()
