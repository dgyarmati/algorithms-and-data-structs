import unittest
from src.python.common_sernse_guide_to_data_structures_and_algorithms.insertion_sort.insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort_sorts_empty_list(self):
        items = []
        expected = []
        insertion_sort(items)
        self.assertEqual(expected, items)

    def test_insertion_sort_sorts_list_with_one_element(self):
        items = [1]
        expected = [1]
        insertion_sort(items)
        self.assertEqual(expected, items)

    def test_insertion_sort_sorts_list_with_two_elements(self):
        items = [1, -2]
        expected = [-2, 1]
        insertion_sort(items)
        self.assertEqual(expected, items)

    def test_insertion_sort_sorts_list_with_n_elements(self):
        items = [1, -2, 22, -234, 0, 12, 0]
        expected = [-234, -2, 0, 0, 1, 12, 22]
        insertion_sort(items)
        self.assertEqual(expected, items)
