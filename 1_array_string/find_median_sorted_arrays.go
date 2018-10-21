package strings

/*
FindMedianSortedArrays There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

This problem can be converted to the problem of finding kth element, k is (A's length + B' Length)/2.
If any of the two arrays is empty, then the kth element is the non-empty array's kth element. If k == 0, the kth element is the first element of A or B.
For normal cases(all other cases), we need to move the pointer at the pace of half of the array size to get log(n) time.


*/
func FindMedianSortedArrays(n1, n2 []int) int {
	return 0
}
