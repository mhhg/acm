package strings

/*
RemoveDuplicate1 Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length. Do not allocate extra space for another array, you must do this in place with constant memory.

For example, given input array A = [1,1,2], your function should return length = 2, and A is now [1,2].

*/
func RemoveDuplicate1(arr []int) (int, []int) {
	i := 0
	for {
		if i >= len(arr)-2 {
			break
		}
		if arr[i] == arr[i+1] && arr[i] == arr[i+2] {
			arr = append(arr[:i], arr[i+1:]...)
		}
		i++
	}
	return len(arr), arr
}
