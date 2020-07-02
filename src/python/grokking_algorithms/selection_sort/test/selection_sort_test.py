import unittest
from src.python.grokking_algorithms.selection_sort import selection_sort


class SelectionSortTest(unittest.TestCase):
    def test_selection_sort_finds_value(self):
        values = [156, 141, 35, 94, 88, 61, 111]
        smallest_value = selection_sort.selection_sort(values)[0]
        self.assertEqual(35, smallest_value)
