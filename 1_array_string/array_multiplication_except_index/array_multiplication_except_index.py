import functools
import operator
from typing import Dict, List
from timeit import timeit

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
        # multiplication = functools.reduce(
        #     operator.mul, wanted_array, 1)
        multiplication = 1
        for j, num2 in enumerate(wanted_array):
            multiplication *= num2

        ret.append(multiplication)
    return ret


def array_multiplication_except_index_optimized(elements: List[int]) -> List[int]:
    N = len(elements)
    if N == 0:
        return

    # Initialzie list of 1, size N
    result = [1]*N

    for i in range(1, N):
        result[i] = result[i-1] * elements[i-1]

    r_prod = 1
    for i in reversed(range(N)):
        result[i] *= r_prod
        r_prod *= elements[i]

    return result


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def benchmark(elements):
    x = timeit(wrapper(array_multiplication_except_index, elements), number=100)
    y = timeit(
        wrapper(array_multiplication_except_index_optimized, elements), number=100)
    print(
        '\n --Benckmark:',
        '\nsolution  (x) :', x,
        '\noptimized (y) :', y,
        '\n        x / y :', x / y,
        '\n--Benckmark Done.\n')


if __name__ == "__main__":
    print(array_multiplication_except_index([1, 2, 3, 4, 5]))
    print(array_multiplication_except_index([3, 2, 1]))
    print(array_multiplication_except_index_optimized([1, 2, 3, 4, 5]))
    print(array_multiplication_except_index_optimized([3, 2, 1]))

    benchmark([3, 2, 1])
    benchmark([1, 2, 3, 4, 5])
    benchmark([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    benchmark([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 43, 65, 78, 25])
