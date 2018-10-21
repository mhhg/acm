import unittest
from two_sum import two_sum


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        pass

    def test_simple(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_simple_2(self):
        self.assertEqual(two_sum([3, 7, 11, 15], 26), [2, 3])

    def test_simple_3(self):
        self.assertEqual(two_sum([3, 7, 12, 15], 18), [0, 3])


if __name__ == '__main__':
    unittest.main()
