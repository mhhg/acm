from typing import Dict, List


"""
TwoSum Given an array of integers, find two numbers such that they add up to
a specific target number.

The function twoSum should return indices of the two numbers such that they add
up to the target, where index1 must be less than index2.

Please note that your returned answers (both index1 and index2) are not
zero-based.


For example:
- Input: numbers={2, 7, 11, 15}, target=9
- Output: index1=0, index2=1
"""


def two_sum(arr: List[int], target: int) -> List[int]:
    temporary_dict: Dict[int, int] = {}

    for index, number in enumerate(arr):
        if number not in temporary_dict:
            temporary_dict[target-number] = index
        else:
            return [temporary_dict[number], index]

    return None
