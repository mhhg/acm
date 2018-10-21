from typing import List, Tuple

"""
Given an array S of n integers, are there elements a, b, c, and d in
S such that a + b + c + d = target?

Find all unique quadruplets in the array which gives the
sum of target.

Note:
- Elements in a quadruplet (a, b, c, d) must be in non-descending order.
(ie, a ≤ b ≤ c ≤ d)

- The solution set must not contain duplicate quadruplets.
"""


def four_sum(elements: List[int], target: int) -> List[Tuple[int]]:
    quadruplets = []
    elements, COUNT = sorted(elements), len(elements)
    for i in range(COUNT-3):
        if i != 0 and elements[i] == elements[i-1]:
            continue
        for j in range(i + 1, COUNT-2):
            if j != i + 1 and elements[j] == elements[j-1]:
                continue
            k, z = j + 1, COUNT - 1
            while k < z:
                sample = (elements[i], elements[j],
                              elements[k], elements[z])
                sample_sum = sum(sample)
                if sample_sum == target:
                    quadruplets.append(sample)
                    k += 1
                    z -= 1
                    while k < z and elements[k] == elements[k-1]:
                        k += 1
                    while k < z and elements[z] == elements[z+1]:
                        z -= 1
                elif sample_sum < target:
                    k += 1
                else:
                    z -= 1
    return quadruplets


def four_sum_2(elements: List[int], target: int) -> List[Tuple[int]]:
    quadruplets, tmp, COUNT = [], {}, len(elements)
    for i in range(COUNT):
        for j in range(COUNT):
            if j == i:
                continue
            for k in range(COUNT):
                if k == j or k == i: 
                    continue
                for z in range(COUNT):
                    if z == k or z == j or z == i:
                        continue
                    sample = tuple(sorted((elements[i], elements[j],
                              elements[k], elements[z])))
                    sample_sum = sum(sample)
                    if sample_sum == target and sample not in tmp:
                        tmp[sample] = 1
                        quadruplets.append(sample)
    return quadruplets
