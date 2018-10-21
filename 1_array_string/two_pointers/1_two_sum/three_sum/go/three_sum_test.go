package threesum

import (
	"reflect"
	"testing"
)

func TestThreeSum(t *testing.T) {
	type args struct {
		elements []int
	}
	tests := []struct {
		name        string
		args        args
		wantResults [][]int
	}{
		{
			name: "ok",
			args: args{
				elements: []int{-1, 0, 1, 2, -1, -4},
			},
			wantResults: [][]int{
				[]int{-1, 0, 1},
				[]int{-1, -1, 2},
			},
		},
		{
			name: "ok2",
			args: args{
				elements: []int{-6, 2, -3, 13, -7, 1},
			},
			wantResults: [][]int{
				[]int{-7, -6, 13},
				[]int{-3, 1, 2},
			},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			gotResults := ThreeSum(tt.args.elements)
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
					t.Errorf("ThreeSum() = %v, want %v", gotResults, tt.wantResults)
				}
			}
		})
	}
}
