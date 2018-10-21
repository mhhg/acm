package foursum

import (
	"sort"
)

/*
FourSum Given an array S of n integers, are there elements a, b, c, and d in
S such that a + b + c + d = target?

Find all unique quadruplets in the array which gives the
sum of target.

Note:
- Elements in a quadruplet (a,b,c,d) must be in non-descending order.
(ie, a ≤ b ≤ c ≤ d)

- The solution set must not contain duplicate quadruplets.
*/
func FourSum(elements []int, target int) (quadruplets [][]int) {
	quadruplets = [][]int{}
	sort.Slice(elements, func(i, j int) bool {
		return elements[i] < elements[j]
	})
	var COUNT = len(elements)
	for i := 0; i < COUNT-3; i++ { // index: (i, j, k, z)
		for j := i + 1; j < COUNT-2; j++ {
			if j != i+1 && elements[j] == elements[j-1] {
				continue
			}
			k, z := j+1, COUNT-1
			for k < z {
				if sum := elements[i] + elements[j] + elements[k] + elements[z]; sum == target {
					quadruplets = append(quadruplets,
						[]int{elements[i], elements[j], elements[k], elements[z]},
					)
					k++
					z--
					for k < z && elements[k] == elements[k-1] {
						k++
					}
					for k < z && elements[z] == elements[z+1] {
						z--
					}
				} else if sum < 0 {
					k++
				} else {
					z--
				}
			}
		}
	}
	return quadruplets
}
