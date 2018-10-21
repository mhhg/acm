import unittest
from two_sum_II import two_sum_II


class TwoSumII(unittest.TestCase):
    def setUp(self):
        pass

    def test_simple(self):
        self.assertEqual(two_sum_II([2, 7, 11, 15], 22), [1, 3])

    def test_simple_2(self):
        self.assertEqual(two_sum_II(
            [2, 7, 11, 15, 23, 43, 54, 65, 463, 894, 1024], 67), [0, 7])

    def test_simple_3(self):
        self.assertEqual(two_sum_II([23, 75, 98, 115, 215, 9487], 313), [2, 4])

    def test_result_does_not_exist(self):
        self.assertEqual(two_sum_II([2, 7, 11, 15], 14), None)


if __name__ == '__main__':
    unittest.main()
