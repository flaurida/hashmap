import unittest
from hash_map import HashMap

# testing suite for various operations in hashmap class
class HashMapTests(unittest.TestCase):
    def setUp(self):
        self.hash_map = HashMap()

    def tearDown(self):
        self.hash_map = None

    # test creation of empty hashmap
    def test_create_hash_map(self):
        self.assertTrue(self.hash_map.is_empty())
        self.assertEqual(len(self.hash_map), 0)

    # test insertion of key into hashmap and getter method
    def test_can_insert_into_hash_map(self):
        self.assertFalse(self.hash_map.has_key("test"))
        self.hash_map["test"] = "testing"
        self.assertTrue(self.hash_map.has_key("test"))
        self.assertEqual(len(self.hash_map), 1)
        self.assertEqual("testing", self.hash_map["test"])

    # test updating of key that already exists in hashmap
    def test_can_update_key_in_hash_map(self):
        self.hash_map["test"] = "testing"
        self.hash_map["test"] = "testing123"
        self.assertEqual("testing123", self.hash_map["test"])

    # test deleting of key in hashmap
    def test_can_delete_key_in_hash_map(self):
        self.hash_map["test"] = "testing"
        self.hash_map.delete("test")
        self.assertFalse(self.hash_map.has_key("test"))
        self.assertIsNone(self.hash_map.get("test"))

    # test that number of buckets grows after number of key/value pairs
    # becomes greater than number of buckets
    def test_hash_map_resize_after_insert(self):
        self.assertEqual(8, self.hash_map.num_buckets())

        i = 1
        while i <= 9:
            self.hash_map[i] = i
            i += 1

        self.assertEqual(16, self.hash_map.num_buckets())

    # test that number of buckets shrinks after number of key/value pairs
    # becomes less than one quarter of the number of buckets
    def test_hash_map_shrink_after_delete(self):
        i = 1
        while i <= 9:
            self.hash_map[i] = i
            i += 1

        while i > 0:
            self.hash_map.delete(i)
            i -= 1

        self.assertEqual(8, self.hash_map.num_buckets())

    # test that update method incorporates key/value pairs of another hashmap
    def test_hash_map_updates_with_other_hash_map(self):
        self.hash_map["test"] = "testing"
        other_hash_map = HashMap()
        other_hash_map["test"] = "testing123"
        other_hash_map["another test"] = "another testing123"
        self.hash_map.update(other_hash_map)
        self.assertEqual("testing123", self.hash_map["test"])
        self.assertEqual(["testing123", "another testing123"], self.hash_map.values())

if __name__ == '__main__':
    unittest.main()
