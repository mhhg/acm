package search

func BinarySearch(list []int, value int) int {
	begin := 0
	end := len(list) - 1
	for begin <= end {
		median := (begin + end) / 2
		if list[median] < value {
			begin = median + 1
		} else {
			end = median - 1
		}
	}
	if begin == len(list) || list[begin] != value {
		return -1
	} else {
		return begin
	}
}
