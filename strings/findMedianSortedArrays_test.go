package strings

import "testing"

func TestFindMedianSortedArrays(t *testing.T) {
	type args struct {
		n1 []int
		n2 []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
	// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := FindMedianSortedArrays(tt.args.n1, tt.args.n2); got != tt.want {
				t.Errorf("FindMedianSortedArrays() = %v, want %v", got, tt.want)
			}
		})
	}
}
