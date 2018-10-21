package foursum

import (
	"fmt"
	"reflect"
	"testing"
)

func TestFourSum(t *testing.T) {
	type args struct {
		elements []int
		target   int
	}
	tests := []struct {
		name        string
		args        args
		wantResults [][]int
	}{
		{
			name: "ok",
			args: args{
				elements: []int{1, 4, -2, -3, 6, -1, 2},
				target:   0,
			},
			wantResults: [][]int{
				[]int{-3, -2, 1, 4},
				[]int{-3, -2, -1, 6},
			},
		},
		{
			name: "ok2",
			args: args{
				elements: []int{1, 4, -2, -3, 6, -1, 2},
				target:   4,
			},
			wantResults: [][]int{
				[]int{-2, -1, 1, 6},
			},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			gotResults := FourSum(tt.args.elements, tt.args.target)
			fmt.Println(gotResults)
			for _, want := range tt.wantResults {
				exists := false
				for j, got := range gotResults {
					if reflect.DeepEqual(want, got) {
						gotResults = append(gotResults[:j], gotResults[j+1:]...)
						exists = true
						break
					}
				}
				if !exists {
					t.Errorf("FourSum() = %v, want %v", gotResults, tt.wantResults)
				}
			}
		})
	}
}
