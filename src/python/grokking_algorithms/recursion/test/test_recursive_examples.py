import unittest
from src.python.grokking_algorithms.recursion.find_key_in_boxes import find_box_with_key
from src.python.grokking_algorithms.recursion.factorial import factorial


class TestRecursiveExamples(unittest.TestCase):
    def test_find_key_in_boxes_finds_key(self):
        box = [[], [], ["key"], []]
        box_with_key = find_box_with_key(box)
        self.assertEqual("key", box_with_key[0])

    def test_factorial(self):
        n = 5
        expected = 120
        actual = factorial(n)
        self.assertEqual(expected, actual)
