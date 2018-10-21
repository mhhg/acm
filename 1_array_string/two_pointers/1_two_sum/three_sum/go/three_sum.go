package threesum

import "sort"

/*
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
*/
func ThreeSum(elements []int) (results [][]int) {
	results = [][]int{}
	// sort elements
	sort.Slice(elements, func(i, j int) bool {
		return elements[i] < elements[j]
	})
	for i := 0; i < len(elements)-2; i++ {
		if i == 0 || elements[i] > elements[i-1] {
			j := i + 1
			k := len(elements) - 1
			for j < k {
				if sum := elements[i] + elements[j] + elements[k]; sum == 0 {
					results = append(results,
						[]int{elements[i], elements[j], elements[k]},
					)
					j++
					k--
					for j < k && elements[j] == elements[j-1] {
						j++
					}
					for j < k && elements[k] == elements[k+1] {
						k--
					}
				} else if sum < 0 {
					j++
				} else {
					k--
				}
			}
		}
	}
	return results
}
