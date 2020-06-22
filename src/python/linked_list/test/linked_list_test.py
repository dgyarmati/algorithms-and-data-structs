import unittest
from src.data_structs.linked_list.linked_list import LinkedList


class LinkedListTest(unittest.TestCase):
    def test_delete_empty_linked_list_raises_exception(self):
        linked_list = LinkedList()
        with self.assertRaises(Exception) as context:
            linked_list.delete_node(1)
        self.assertTrue("Linked List is empty!" in str(context.exception))

    def test_delete_head_node_returns_deleted_node(self):
        linked_list = LinkedList([1, 2, 3, 4])
        deleted_node = linked_list.delete_node(1)
        self.assertEqual(deleted_node.data, 1)

    def test_delete_head_node_changes_reference(self):
        linked_list = LinkedList([1, 2, 3, 4])
        linked_list.delete_node(1)
        expected = LinkedList([2, 3, 4])
        self.assertEqual(linked_list, expected)

    def test_delete_node_returns_deleted_node(self):
        linked_list = LinkedList([1, 2, 3, 4])
        deleted_node = linked_list.delete_node(3)
        self.assertEqual(deleted_node.data, 3)

    def test_delete_node_changes_reference(self):
        linked_list = LinkedList([1, 2, 3, 4])
        linked_list.delete_node(3)
        expected = LinkedList([1, 2, 4])
        self.assertEqual(expected, linked_list)

    def test_delete_last_node_returns_deleted_node(self):
        linked_list = LinkedList([1, 2, 3, 4])
        deleted_node = linked_list.delete_node(4)
        self.assertEqual(deleted_node.data, 4)

    def test_delete_last_node_changes_reference(self):
        linked_list = LinkedList([1, 2, 3, 4])
        linked_list.delete_node(4)
        expected = LinkedList([1, 2, 3])
        self.assertEqual(expected, linked_list)

    def test_remove_dups(self):
        linked_list = LinkedList([1, 2, 2, 4])
        linked_list.remove_duplicates()
        linked_list_repr = linked_list.__repr__()
        expected_repr = "1 -> 2 -> 4"
        self.assertEqual(expected_repr, linked_list_repr)

    def test_remove_dups_no_buffer(self):
        linked_list = LinkedList([1, 1, 2, 3, 4])
        linked_list.remove_duplicates_with_runner()
        linked_list_repr = linked_list.__repr__()
        expected_repr = "1 -> 2 -> 3 -> 4"
        self.assertEqual(expected_repr, linked_list_repr)

    def test_kth_to_last(self):
        linked_list = LinkedList([1, 1, 2, 3, 4])
        kth_node = linked_list.get_kth_to_last(2)

        expected_values = "234"
        actual_values = ""
        node = kth_node
        while node:
            actual_values += str(node.data)
            node = node.next

        self.assertEqual(expected_values, actual_values)


