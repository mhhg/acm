import unittest
from timeit import timeit

from four_sum import four_sum, four_sum_2


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def benchmark(elements, target):
    x = timeit(wrapper(four_sum_2, elements, target), number=100)
    y = timeit(wrapper(four_sum, elements, target), number=100)
    print(
        '\n --Benckmark:',
        '\nfour_sum_2 (x) :', x,
        '\nfour_sum   (y) :', y,
        '\n         x / y :', x / y,
        '\n--Benckmark Done.\n')


class TestFourSum(unittest.TestCase):
    def setUp(self):
        pass

    def test_ok(self):
        elements = [1, 4, -2, -3, 6, -1, 2]
        target = 0
        wanted = set([
            (-3, -2, -1, 6),
            (-2, -1, 1, 2),
            (-3, -2, 1, 4),
        ])

        self.assertEqual(set(four_sum(elements, target)), wanted)
        self.assertEqual(set(four_sum_2(elements, target)), wanted)
        benchmark(elements, target)

    def test_ok_2(self):
        elements = [-15, -46, 0, -1, 12, 4, 2, 30, 27, 19, 40, -6, -9, -12]
        target = -19
        wanted = set([
            (-46, -15, 2, 40),
            (-46, -15, 12, 30),
            (-46, -12, -1, 40),
            (-15, -6, 0, 2),
            (-46, -12, 12, 27),
            (-12, -9, 0, 2),
            (-12, -6, -1, 0),
        ])

        self.assertEqual(set(four_sum(elements, target)), wanted)
        self.assertEqual(set(four_sum_2(elements, target)), wanted)

        benchmark(elements, target)

    def test_ok_3(self):
        elements = [1, 4, -2, -3, 6, -1, 2, 3, 13, 3]
        target = 7
        wanted = set([
            (-2, 2, 3, 4),
            (-3, 3, 3, 4),
            (-3, -2, -1, 13),
            (-1, 2, 3, 3),
            (-2, 1, 2, 6),
            (-3, 1, 3, 6),
            (-1, 1, 3, 4),
            (-2, -1, 4, 6),
        ])

        self.assertEqual(set(four_sum(elements, target)), wanted)
        self.assertEqual(set(four_sum_2(elements, target)), wanted)

        benchmark(elements, target)
