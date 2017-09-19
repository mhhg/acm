package strings

// Rotate an array of n elements to the right by k steps.
// with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4]
func Rotate(nums []int, k int) (result []int) {
	if k > len(nums) {
		k = k % len(nums)
	}
	result = make([]int, len(nums))
	for i := 0; i < k; i++ {
		result[i] = nums[len(nums)-k+i]
	}
	for i, j := k, 0; i < len(nums); i++ {
		result[i] = nums[j]
		j++
	}
	return
}