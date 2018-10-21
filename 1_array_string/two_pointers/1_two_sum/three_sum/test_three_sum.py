import unittest

from three_sum import three_sum, ThreeSum


class TestThreeSum(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        data = [-1, 0, 1, 2, -1, 4]
        wanted = set([(-1, 0, 1), (-1, -1, 2)])

        self.assertSetEqual(three_sum(data), wanted)
        self.assertSetEqual(ThreeSum(data).solve(), wanted)

    def test_2(self):
        data = [-1, 1, 12, -6, 0, -6, -13, 5, -1, 2]
        wanted = set([
            (-6, -6, 12), (-13, 1, 12),
            (-6, 1, 5), (-1, -1, 2),
            (-1, 0, 1)
        ])

        self.assertSetEqual(three_sum(data), wanted)
        self.assertSetEqual(ThreeSum(data).solve(), wanted)

    def test_3(self):
        data = [-23, -41, -11, 4, 2, 14, 1, 3, 1, 4, 34, 5, 21, 20, 40]
        wanted = set([
            (-23, 2, 21), (-23, -11, 34),
            (-41, 1, 40), (-41, 20, 21),
            (-23, 3, 20)
        ])

        self.assertSetEqual(three_sum(data), wanted)
        self.assertSetEqual(ThreeSum(data).solve(), wanted)


if __name__ == "__main__":
    unittest.main()
