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

def min_two_sub_arr_sum(elements: List[int], s: int) -> int:
    if sum(elements) < s:
        return 0

    elements = sorted(elements)
    if elements[-1] < s:
        elements = elements[::-1]

    for length in range(2, len(elements)):
        for i, n in enumerate(elements[:-length+1]):
            # print(i, length, elements[i:i+length], sum(elements[i:i+length]))
            if sum(elements[i:i+length]) >= s:
                return length

    return 0