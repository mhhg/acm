import unittest
from max_size_subarray_sum import max_size_subarray_sum_eq_k


class TestMaxSizeSubarraySum(unittest.TestCase):
    def setUp(self):
        pass

    def test_ok_1(self):
        nums = [1, -1, 5, -2, 3]
        k = 3
        self.assertEqual(max_size_subarray_sum_eq_k(nums, k), 4)
