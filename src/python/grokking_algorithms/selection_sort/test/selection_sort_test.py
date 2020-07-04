import unittest
from src.python.grokking_algorithms.selection_sort import selection_sort


class SelectionSortTest(unittest.TestCase):
    def test_selection_sort_finds_value(self):
        items = [156, 141, 35, 94, 88, 61, 111]
        expected = [35, 61, 88, 94, 111, 141, 156]
        selection_sort(items)
        self.assertEqual(expected, items)
