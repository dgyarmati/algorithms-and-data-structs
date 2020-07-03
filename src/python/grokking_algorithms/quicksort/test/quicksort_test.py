import random
import unittest

from src.python.grokking_algorithms.quicksort.quicksort import quicksort


class QuicksortTest(unittest.TestCase):
    def test_quicksort_returns_empty_list_when_sorting_empty_list(self):
        items = []
        expected = []
        actual = quicksort(items)
        self.assertEqual(expected, actual)

    def test_quicksort_returns_one_element_list_when_sorting_one_element_list(self):
        items = [1]
        expected = [1]
        actual = quicksort(items)
        self.assertEqual(expected, actual)

    def test_quicksort_sorts_numbers_of_two_element_list(self):
        items = [4, 1]
        expected = [1, 4]
        actual = quicksort(items)
        self.assertEqual(expected, actual)

    def test_quicksort_does_not_sort_sorted_list(self):
        items = [1, 4]
        expected = [1, 4]
        actual = quicksort(items)
        self.assertEqual(expected, actual)

    def test_quicksort_sorts_numbers_of_three_element_list(self):
        items = [4, 1, -12]
        expected = [-12, 1, 4]
        actual = quicksort(items)
        self.assertEqual(expected, actual)

    def test_quicksort_sorts_numbers_of_arbitrary_element_list(self):
        items = generate_random_list()
        actual = quicksort(items)
        expected = sorted(items)
        self.assertEqual(expected, actual)


def generate_random_list():
    length = random.randint(2, 300)
    return [random.randint(-300, 1000) for _ in range(length)]
