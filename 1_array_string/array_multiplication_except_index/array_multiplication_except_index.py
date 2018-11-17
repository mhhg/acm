from typing import List, Dict
from collections import OrderedDict
import operator
import functools


"""
Given an array of integers, return a new array such that each element at
index `i` of the new array is the product of all the numbers in the original
array except the one at `i`.

for example:
    1. input [1, 2, 3, 4, 5],
    -  the excepted output would be [120, 60, 40, 30, 24].
    2. input [3, 2, 1],
    -  the excepted output would be [2, 3, 6].

"""


def array_multiplication_except_index(elements: List[int]) -> List[int]:
    ret: List[int] = []
    for i, num1 in enumerate(elements):
        wanted_array = elements[0:i] + elements[i+1:]
        multiplication = functools.reduce(
            operator.mul, wanted_array, 1)
        ret.append(multiplication)
    return ret


if __name__ == "__main__":
    print(array_multiplication_except_index([1, 2, 3, 4, 5]))
    print(array_multiplication_except_index([3, 2, 1]))
