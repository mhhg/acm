import unittest

from two_sum_III import TwoSum


def make_two_sum(numbers):
    ts = TwoSum()
    for v in numbers:
        ts.add(v)
    return ts


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.two_sum = make_two_sum([1, 3, 5])

    def test_add(self):
        self.two_sum.add(6)

    def test_find(self): 
        self.assertEqual(self.two_sum.find(4), True, "Should exists!")
        self.assertEqual(self.two_sum.find(7), True, "Should not exists!")


if __name__ == '__main__':
    unittest.main()
