import unittest
from src.python.common_sernse_guide_to_data_structures_and_algorithms.bubble_sort.bubble_sort import bubble_sort
from src.python.common_sernse_guide_to_data_structures_and_algorithms.bubble_sort.bubble_sort import recursive_bubble_sort


class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort_sorts_two_elements(self):
        items = [8, -12]
        expected = [-12, 8]
        bubble_sort(items)
        self.assertEqual(expected, items)

    def test_bubble_sort_sorts_elements(self):
        items = [3, 12, -80, 3, 8]
        expected = [-80, 3, 3, 8, 12]
        bubble_sort(items)
        self.assertEqual(expected, items)

    def test_bubble_sort_sorts_one_element(self):
        items = [1]
        bubble_sort(items)
        self.assertEqual([1], items)

    def test_bubble_sort_sorts_empty_elements(self):
        items = []
        bubble_sort(items)
        self.assertEqual([], items)

    def test_recursive_bubble_sort_sorts_two_elements(self):
        items = [8, -12]
        expected = [-12, 8]
        recursive_bubble_sort(items, len(items))
        self.assertEqual(expected, items)

    def test_recursive_bubble_sort_sorts_elements(self):
        items = [3, 12, -80, 3, 8]
        expected = [-80, 3, 3, 8, 12]
        recursive_bubble_sort(items, len(items))
        self.assertEqual(expected, items)

    def test_recursive_bubble_sort_sorts_one_element(self):
        items = [1]
        recursive_bubble_sort(items, len(items))
        self.assertEqual([1], items)

    def test_recursive_bubble_sort_sorts_empty_elements(self):
        items = []
        recursive_bubble_sort(items, len(items))
        self.assertEqual([], items)
