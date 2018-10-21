package twosum3

/*
TwoSumIII Design and implement a TwoSum class.

It should support the following operations: add and find.

- add: Add the number to an internal data structure.
- find: Find if there exists any pair of numbers which sum is equal to the value.

-For example:
- add(1);
- add(3);
- add(5);
- find(4) -> true
- find(7) -> false
*/
func TwoSumIII() {

}

// ITwoSum is the interface which supports given functionality
type ITwoSum interface {
	Add(num int)
	Find(value int) bool
}

// TwoSum is the main object
type TwoSum struct {
	elements map[int]int // key is added number, value is the occurrence repetition
}

// NewTwoSum makes a new two sum object
func NewTwoSum(values ...int) *TwoSum {
	t := TwoSum{
		elements: make(map[int]int),
	}
	for _, v := range values {
		t.elements[v] = 1
	}
	return &t
}

// Add the number to an internal data structure.
func (ts *TwoSum) Add(num int) {
	if n, ok := ts.elements[num]; ok {
		ts.elements[num] = n + 1
	} else {
		ts.elements[num] = 1
	}
}

// Find if there exists any pair of numbers which sum is equal to the value.
func (ts *TwoSum) Find(value int) bool {
	for key, rep := range ts.elements {
		target := value - key
		if _, ok := ts.elements[target]; ok {
			if key == target && rep < 2 {
				continue
			}
			return true
		}
	}
	return false
}
