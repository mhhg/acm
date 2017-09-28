package main

var minSeqLen = 4

// return the node between a and b if there is one, or 0.
func middle(a, b int) int {
	if (a+b)%2 != 0 {
		return 0
	}
	if mid := (a + b) / 2; mid == 5 || a%3 == b%3 || (a-1)/3 == (b-1)/3 {
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
	for i := range x {
		if !contains(i, base) {
			mid := middle(i, base[len(base)-1])
			if mid == 0 || contains(mid, base) {
				tmp = append(tmp, mid)
			}
		}
	}
	return tmp
}

func contains(i int, items []int) bool {
	for _, x := range items {
		if i == x {
			return true
		}
	}
	return false
}

func sequence(base []int) [][]int {
	if len(base) >= minSeqLen {
		return [][]int{base}
	}
	x := [][]int{}
	for _, n := range next(base) {
		base = append(base, n)
		for _, s := range sequence(base) {
			x = append(x, s)
		}
	}
	return x
}

func main() {
	seqs := []int{0, 0, 0, 0, 0, 0, 0, 0, 0}
	for _, s := range sequence([]int{}) {
		seqs[len(s)] += 1
	}
}
