from typing import List

"""
Given an array nums and a target value k, find the maximum length of a 
subarray that sums to k. If there isn't one, return 0 instead.

Note:
- The sum of the entire nums array is guaranteed to fit within the 32-bit 
  signed integer range.


Example 1:
- Given nums = [1, -1, 5, -2, 3], k = 3,
- return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)
"""


def max_size_subarray_sum_eq_k(nums: List[int], k: int) -> int:
    _sum = sum(nums)
    if _sum < k:
        return 0
    elif _sum == k:
        return len(nums)

    nums = sorted(nums)  # -2, -1, 1, 3, 5 sum = 6 - 3 = 3
    for i, n in enumerate(nums):
        if sum(nums) - n == k:
            return len(nums) - 1

    return 0
