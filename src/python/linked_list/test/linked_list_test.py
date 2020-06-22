import unittest
from src.data_structs.linked_list.linked_list import LinkedList
from src.data_structs.linked_list.linked_list import Node
from src.data_structs.linked_list.linked_list import is_intersection_present
from src.data_structs.linked_list.linked_list import sum_linked_lists_reverse


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

    def test_kth_to_last_returns_correct_value(self):
        linked_list = LinkedList([1, 1, 2, 3, 4])
        expected_node = Node(3)
        actual_node = linked_list.get_kth_to_last(2)
        self.assertEqual(expected_node, actual_node)

    def test_kth_to_last_returns_none_if_value_does_not_exist(self):
        linked_list = LinkedList([1, 1, 2, 3, 4])
        expected_node = None
        actual_node = linked_list.get_kth_to_last(10)
        self.assertEqual(expected_node, actual_node)

    def test_print_kth_to_last(self):
        linked_list = LinkedList([1, 1, 2, 3, 4])
        linked_list.print_kth_to_last(linked_list.head, 3)

    def test_delete_middle_node(self):
        linked_list = LinkedList([1, 1, 2, 3, 4])
        node = linked_list.find(2)
        linked_list.delete_middle_node(node)
        self.assertEqual("1 -> 1 -> 3 -> 4", linked_list.__repr__())

    def test_linked_list_is_palindrome_returns_true(self):
        linked_list = LinkedList(["n", "u", "r", "s", "e", "s", "r", "u", "n"])
        self.assertTrue(linked_list.is_palindrome())

    def test_linked_list_is_palindrome_returns_false(self):
        linked_list = LinkedList(["w", "o", "l", "f"])
        k = linked_list.is_palindrome()
        self.assertFalse(linked_list.is_palindrome())

    def test_is_intersection_present_returns_true(self):
        common_node = Node(8)
        linked_list_1 = LinkedList()

        linked_list_1.head = common_node
        linked_list_1.append(1)
        linked_list_1.append(2)
        linked_list_1.append(3)

        linked_list_2 = LinkedList()
        linked_list_2.append(4)
        linked_list_2.head.next = common_node
        linked_list_2.append(5)
        linked_list_2.append(6)

        self.assertTrue(is_intersection_present(linked_list_1, linked_list_2))

    def test_is_intersection_present_returns_false(self):
        linked_list_1 = LinkedList([1, 1, 2, 3, 4])
        linked_list_2 = LinkedList([1, 1, 2, 3, 4])

        self.assertFalse(is_intersection_present(linked_list_1, linked_list_2))

    def test_get_circular_loop_head_returns_true(self):
        linked_list = LinkedList([1, 2, 3])
        linked_list.head.next.next.next = linked_list.head

        self.assertEqual(linked_list.get_circular_loop_head().data, 1)

    def test_get_circular_loop_head_returns_false(self):
        linked_list = LinkedList([1, 2, 3, 4])

        self.assertIsNone(linked_list.get_circular_loop_head())

    def test_sum_linked_lists_reverse(self):
        linked_list_1 = LinkedList([7, 1, 6])
        linked_list_2 = LinkedList([5, 9, 2])
        expected = LinkedList([2, 1, 9])
        self.assertEqual(expected, sum_linked_lists_reverse(linked_list_1, linked_list_2))




