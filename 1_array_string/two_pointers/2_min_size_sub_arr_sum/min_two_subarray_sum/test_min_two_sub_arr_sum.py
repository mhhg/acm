import unittest
from min_two_sub_arr_sum import min_two_sub_arr_sum


class TestMinTwoSubArraySum(unittest.TestCase):
    def setUp(self):
        pass

    def test_should_be_zero(self):
        elements = (2, 3, 1, 2, 4, 3)
        s = 17

        self.assertEqual(min_two_sub_arr_sum(elements, s), 0)

    def test_ok_1(self):
        elements = (2, 3, 1, 2, 1, 10)
        s = 6

        self.assertEqual(min_two_sub_arr_sum(elements, s), 1)

    def test_ok_2(self):
        elements = (2, 3, 1, 2, 4, 3)
        s = 7

    def test_ok_3(self):
        elements = (2, 3, 1, 2, 4, 3)
        s = 9

        self.assertEqual(min_two_sub_arr_sum(elements, s), 3)

    def test_ok_4(self):
        elements = (2, 3, 1, 2, 4, 3)
        s = 12

        self.assertEqual(min_two_sub_arr_sum(elements, s), 4)

    def test_ok_5(self):
        elements = (2, 3, 1, 2, 4, 3)
        s = 14

        self.assertEqual(min_two_sub_arr_sum(elements, s), 5)
