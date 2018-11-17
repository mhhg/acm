import unittest
from timeit import timeit

from array_multiplication_except_index import array_multiplication_except_index


class TestArrayMultiplicationExceptIndex(unittest.TestCase):
    def setUp(self):
        pass

    def test_ok(self):
        elements = [1, 2, 3, 4, 5]
        wanted = set([120, 60, 40, 30, 24])

        self.assertEqual(
            set(array_multiplication_except_index(elements)), wanted)

    def test_ok_2(self):
        elements = [3, 2, 1]
        wanted = set([2, 3, 6])

        self.assertEqual(
            set(array_multiplication_except_index(elements)), wanted)


if __name__ == "__main__":
    unittest.main()
