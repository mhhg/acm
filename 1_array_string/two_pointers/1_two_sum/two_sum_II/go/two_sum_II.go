package twosum2

/*
TwoSumII Input array is sorted

This problem is similar to Two Sum but the input array is sorted.

We can use two points to scan the array from both sides.
*/
func TwoSumII(arr []int, target int) []int {
	// tmp := make(map[int]int) // number, index
	for i, j := 0, len(arr)-1; i < j; {
		x := arr[i] + arr[j]
		if x < target {
			i++
		} else if x > target {
			j--
		} else {
			return []int{i, j}
		}
	}
	return nil
}
