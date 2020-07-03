import random
import unittest

from src.python.grokking_algorithms.quicksort.quicksort import quicksort


class QuicksortTest(unittest.TestCase):
    def test_quicksort_returns_empty_list_when_sorting_empty_list(self):
        items = []
        expected = []
        quicksort(items, 0, len(items) - 1)
        self.assertEqual(expected, items)

    def test_quicksort_returns_one_element_list_when_sorting_one_element_list(self):
        items = [1]
        expected = [1]
        quicksort(items, 0, len(items) - 1)
        self.assertEqual(expected, items)

    def test_quicksort_sorts_numbers_of_two_element_list(self):
        items = [4, 1]
        expected = [1, 4]
        quicksort(items, 0, len(items) - 1)
        self.assertEqual(expected, items)

    def test_quicksort_does_not_sort_sorted_list(self):
        items = [1, 4]
        expected = [1, 4]
        quicksort(items, 0, len(items) - 1)
        self.assertEqual(expected, items)

    def test_quicksort_sorts_numbers_of_three_element_list(self):
        items = [4, 1, -12]
        expected = [-12, 1, 4]
        quicksort(items, 0, len(items) - 1)
        self.assertEqual(expected, items)

    def test_quicksort_sorts_numbers_of_four_element_list(self):
        items = [4, 1, -1, -12]
        expected = [-12, -1, 1, 4]
        quicksort(items, 0, len(items) - 1)
        self.assertEqual(expected, items)

    def test_quicksort_sorts_numbers_list(self):
        items = [29, 99, 27, 41, 66, 28, 44, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12, 21, 44]
        expected = [12, 19, 21, 27, 28, 29, 31, 41, 44, 44, 58, 66, 76, 78, 83, 87, 88, 97, 99]
        quicksort(items, 0, len(items) - 1)
        self.assertEqual(expected, items)

    def test_quicksort_sorts_numbers_of_arbitrary_element_list(self):
        items = generate_random_list()
        quicksort(items, 0, len(items) - 1)
        expected = sorted(items)
        self.assertEqual(expected, items)


def generate_random_list():
    length = random.randint(2, 300)
    return [random.randint(-300, 1000) for _ in range(length)]
