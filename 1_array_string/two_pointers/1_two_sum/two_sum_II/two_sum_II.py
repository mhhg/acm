from typing import Dict, List


"""
# Two Sum II Input array is sorted

This problem is similar to Two Sum but the input array is sorted.

We can use two points to scan the array from both sides.

"""


def two_sum_II(input_array: List[int], target: int) -> List[int]:
    begin_index, end_index = 0, len(input_array)-1

    while begin_index < end_index:
        sample_sum = input_array[begin_index] + input_array[end_index]

        if sample_sum < target:
            begin_index += 1
        elif sample_sum > target:
            end_index -= 1
        else:
            return [begin_index, end_index]

    return None
