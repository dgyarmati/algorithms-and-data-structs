import unittest
from src.python.common_sernse_guide_to_data_structures_and_algorithms.find_duplicates.has_duplicates import has_duplicates
from src.python.common_sernse_guide_to_data_structures_and_algorithms.find_duplicates.has_duplicates import has_duplicates_with_buffer


class TestHasDuplicates(unittest.TestCase):
    def test_has_duplicates_returns_true(self):
        items = [12, 3, 1, 2, 1, 1]
        self.assertTrue(has_duplicates(items))

    def test_has_duplicates_returns_false(self):
        items = [12, 3, 1, 2, 10, 13]
        self.assertFalse(has_duplicates(items))

    def test_has_duplicates_returns_false_for_empty_list(self):
        items = []
        self.assertFalse(has_duplicates(items))

    def test_has_duplicates_with_buffer_returns_true(self):
        items = [12, 3, 1, 2, 1, 1]
        self.assertTrue(has_duplicates_with_buffer(items))

    def test_has_duplicates_with_buffer_returns_false(self):
        items = [12, 3, 1, 2, 10, 13]
        self.assertFalse(has_duplicates_with_buffer(items))

    def test_has_duplicates_with_buffer_returns_false_for_empty_list(self):
        items = []
        self.assertFalse(has_duplicates_with_buffer(items))


