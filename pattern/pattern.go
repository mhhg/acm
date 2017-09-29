package pattern

import "fmt"

var (
	sequences [][]int
	min       = 4
)

// return the node between a and b if there is one, or 0.
func middle(a, b int) int {
	if (a+b)%2 != 0 {
		return 0
	}
	if mid := (a + b) / 2; (mid == 5) || (a%3 == b%3) || ((a-1)/3 == (b-1)/3) {
		return mid
	}
	return 0
}

// generate valid moves j+1 given a sequence of moves 1..j.
func next(base []int) []int {
	x := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
	if n := len(base); n >= 9 {
		return nil
	} else if n == 0 {
		return x
	}
	tmp := []int{}
	for _, i := range x {
		if !contains(i, base) {
			if mid := middle(i, base[len(base)-1]); mid == 0 || contains(mid, base) {
				tmp = append(tmp, i)
			}
		}
	}
	return tmp
}

// check if array contains a number or not
func contains(i int, items []int) bool {
	for _, x := range items {
		if i == x {
			return true
		}
	}
	return false
}

// generate valid sequences recursively
func generate(base []int) {
	for _, n := range next(base) {
		s := append(base, n)
		sequences = append(sequences, s)
		generate(s)
	}
}

// calculate sum of an array
func sum(arr []int) (s int) {
	s = 0
	for _, x := range arr {
		s += x
	}
	return
}

// count all valid sequence by length and calculate sum of them
func count() (lengths []int, total int) {
	sequences = make([][]int, 0)
	generate([]int{})
	lengths = []int{0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
	for _, s := range sequences {
		if len(s) >= min {
			lengths[len(s)]++
		}
	}
	fmt.Println(
		"length:", lengths,
		"total:", sum(lengths))
	return lengths, sum(lengths)
}
