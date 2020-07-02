import unittest
from src.python.grokking_algorithms.recursion.find_key_in_boxes import find_box_with_key
from src.python.grokking_algorithms.recursion.factorial import factorial
from src.python.grokking_algorithms.recursion.sum import sum_values
from src.python.grokking_algorithms.recursion.count import count_items
from src.python.grokking_algorithms.recursion.find_maximum_number import find_maximum_number
from src.python.grokking_algorithms.recursion.recursive_binary_search import binary_search


class TestRecursiveExamples(unittest.TestCase):
    def test_find_key_in_boxes_finds_key(self):
        box = [[], [], ["key"], []]
        box_with_key = find_box_with_key(box)
        self.assertEqual("key", box_with_key[0])

    def test_find_key_in_boxes_returns_none_with_empty_boxes(self):
        box = [[], [], [], []]
        box_with_key = find_box_with_key(box)
        self.assertIsNone(box_with_key)

    def test_factorial(self):
        n = 5
        expected = 120
        actual = factorial(n)
        self.assertEqual(expected, actual)

    def test_sum_returns_sum_of_values(self):
        values = [1, 2, 3]
        expected = 6
        actual = sum_values(values)
        self.assertEqual(expected, actual)

    def test_sum_returns_zero_on_empty_array(self):
        values = []
        expected = 0
        actual = sum_values(values)
        self.assertEqual(expected, actual)

    def test_count_items_returns_valid_count(self):
        items = [1, 2, 3, 4, 5]
        expected = 5
        actual = count_items(items)
        self.assertEqual(expected, actual)

    def test_find_maximum_number_returns_maximum_number(self):
        numbers = [1, 0, -3, 4, 245]
        expected = 245
        actual = find_maximum_number(numbers)
        self.assertEqual(expected, actual)

    def test_recursive_binary_search_finds_value_index(self):
        numbers = [1, 2, 3, 4, 5]
        expected = [0, 1, 2, 3, 4]
        actual = [binary_search(numbers, number) for number in numbers]
        self.assertEqual(expected, actual)

    def test_recursive_binary_search_returns_none_if_value_is_not_present(self):
        numbers = [1, 2, 3, 4, 5]
        expected = None
        actual = binary_search(numbers, 8)
        self.assertEqual(expected, actual)
