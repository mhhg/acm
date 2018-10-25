from typing import List


"""
Given an array of n positive integers and a positive integer s,
find the minimal length of a sub-array of which the sum ≥ s.

If there isn't one, return 0 instead.

For example:

- Given the array [2,3,1,2,4,3] and s = 7,
- The sub-array [4,3] has the minimal length of "2"
 
 under the problem constraint.

"""


def min_two_sub_arr_sum(elements: List[int], target: int) -> int:
    if sum(elements) < target:
        return 0

    elements = sorted(elements, reverse=True)

    for length in range(1, len(elements)):
        # print('\n', length, elements[:length], sum(elements[:length]))
        if sum(elements[:length]) >= target:
            return length

    return 0
