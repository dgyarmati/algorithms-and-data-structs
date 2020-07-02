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

    def test_binary_search_speed_is_log_n(self):
        numbers = [1, 2, 3, 8, 12, 24, 32, 64]
        idx, speed = binary_search.gauge_binary_search_speed(numbers, 64)
        # binary search speed is O(log2N); for this list, the worst case is 3 because we have 8 elements, and log 2 8 = 3 (2^3 = 8)
        best_case_speed = 1
        worst_case_speed = 3
        self.assertEqual(7, idx)
        self.assertTrue(speed <= worst_case_speed and speed >= best_case_speed)
