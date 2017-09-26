package sort

// InsertionSort o(n2)
func InsertionSort(list []int) []int {
	for i := 1; i < len(list); i++ {
		if list[i] < list[i-1] {
			tmp := list[i-1]
			list[i-1] = list[i]
			list[i] = tmp
			for j := i - 1; j > 0; j-- {
				if list[j] < list[j-1] {
					tmp := list[j-1]
					list[j-1] = list[j]
					list[j] = tmp
				}
			}
		}
	}
	return list
}
