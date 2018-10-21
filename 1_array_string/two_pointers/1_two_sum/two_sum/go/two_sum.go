package twosum

/*
TwoSum Given an array of integers, find two numbers such that they add up to
a specific target number.

The function twoSum should return indices of the two numbers such that they add
up to the target, where index1 must be less than index2.

Please note that your returned answers (both index1 and index2) are not
zero-based.


For example:
 - Input: numbers={2, 7, 11, 15}, target=9
 - Output: index1=0, index2=1
*/
func TwoSum(arr []int, target int) []int {
	var tmp map[int]int
	tmp = make(map[int]int)
	for i, n := range arr {
		if idx, ok := tmp[n]; !ok {
			tmp[target-n] = i
		} else {
			return []int{idx, i}
		}
	}
	return nil
}
