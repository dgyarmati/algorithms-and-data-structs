import unittest

from src.python.common_sernse_guide_to_data_structures_and_algorithms.find_intersection.find_intersection import find_intersection


class TestFindIntersection(unittest.TestCase):
    def test_find_intersection_finds_intersection_of_two_arrays_assuming_arrays_have_equal_size(self):
        array_1 = [2, 8, 1]
        array_2 = [5, 8, 3]
        expected = [8]
        actual = find_intersection(array_1, array_2)
        self.assertEqual(expected, actual)