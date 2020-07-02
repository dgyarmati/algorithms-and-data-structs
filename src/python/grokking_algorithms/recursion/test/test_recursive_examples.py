import unittest
from src.python.grokking_algorithms.recursion.find_key_in_boxes import find_box_with_key
from src.python.grokking_algorithms.recursion.factorial import factorial
from src.python.grokking_algorithms.recursion.sum import sum_values
from src.python.grokking_algorithms.recursion.count import count_items


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
