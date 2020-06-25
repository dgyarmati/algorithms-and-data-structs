import unittest
from src.python.grokking_algorithms.binary_search import binary_search


class BinarySearchTest(unittest.TestCase):
    def test_binary_search_works_on_first_pass(self):
        numbers = [1, 2, 3, 8, 12, 24]
        idx = binary_search.binary_search(numbers, 8)
        self.assertEqual(3, idx)

    def test_binary_search_works_on_second_pass(self):
        numbers = [1, 2, 3, 8, 12, 24]
        idx = binary_search.binary_search(numbers, 3)
        self.assertEqual(2, idx)

    def test_binary_search_works_on_last_value(self):
        numbers = [1, 2, 3, 8, 12, 24]
        idx = binary_search.binary_search(numbers, 24)
        self.assertEqual(5, idx)

    def test_binary_search_works_on_first_value(self):
        numbers = [1, 2, 3, 8, 12, 24]
        idx = binary_search.binary_search(numbers, 1)
        self.assertEqual(0, idx)

    def test_binary_search_works_on_value_not_in_list(self):
        numbers = [1, 2, 3, 8, 12, 24]
        idx = binary_search.binary_search(numbers, 1113)
        self.assertEqual(None, idx)
