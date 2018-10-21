from typing import List, Set

"""
ThreeSum Given an array S of n integers, are there elements a, b, c in
S such that a + b + c = 0 ?

Find all unique triplets in the array which gives the sum of zero.

    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)

Note:
- Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
- The solution set must not contain duplicate triplets.
"""

# in classic form


def three_sum(elements: List[int]) -> Set[int]:
    result = []
    elements = sorted(elements)
    for index, number in enumerate(elements[:-2]):
        if index == 0 or elements[index] > elements[index-1]:
            j, k = index + 1, len(elements)-1
            while j < k:
                sample = (elements[index], elements[j], elements[k])
                sample_sum = sum(sample)
                if sample_sum == 0:
                    result.append(sample)
                    j += 1
                    k -= 1
                    while elements[j] == elements[k]:
                        j += 1
                    while elements[k] == elements[k+1]:
                        k -= 1
                elif sample_sum < 0:
                    j += 1
                else:
                    k -= 1
    return set(result)

# in OOP form


class ThreeSum(object):
    def __init__(self, elements: List[int]):
        self.array = sorted(elements)
        self.count = len(elements)
        self.result = []
        self._latest_sample = []
        self._latest_sum = -1

    def solve(self) -> Set[int]:
        for index, number in enumerate(self.array[:-2]):
            if index == 0 or number > self.array[index-1]:
                self._set_counters(index)
                self._find_two_others(index)
        return set(self.result)

    def _find_two_others(self, index: int):
        while self.j < self.k:
            self._checkout_state(index)
            self._update_counters()

    def _set_counters(self, index: int):
        self.j, self.k = index + 1, self.count - 1

    def _checkout_state(self, index: int):
        if self._does_sum_equals_zero(index, self.j, self.k):
            self.result.append(self._latest_sample)

    def _does_sum_equals_zero(self, i: int, j: int, k: int):
        self._latest_sample = (self.array[i], self.array[j], self.array[k])
        self._latest_sum = sum(self._latest_sample)

        if self._latest_sum == 0:
            return True

        return False

    def _update_counters(self):
        if self._latest_sum == 0:
            self._normal_counter_change()
        elif self._latest_sum < 0:
            self.j += 1
        else:
            self.k -= 1

    def _normal_counter_change(self):
        j, k = self.j + 1, self.k - 1

        while self.array[j] == self.array[j - 1]:
            j += 1

        while self.array[k] == self.array[k+1]:
            k -= 1

        self.j, self.k = j, k
