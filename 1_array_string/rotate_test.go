package strings

import (
	"reflect"
	"testing"
)

func TestRotate(t *testing.T) {
	type args struct {
		nums []int
		k    int
	}
	tests := []struct {
		name       string
		args       args
		wantResult []int
	}{
		{
			"hello",
			args{
				[]int{1, 2, 3, 4, 5, 6, 7},
				3,
			},
			[]int{5, 6, 7, 1, 2, 3, 4},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if gotResult := Rotate(tt.args.nums, tt.args.k); !reflect.DeepEqual(gotResult, tt.wantResult) {
				t.Errorf("Rotate() = %v, want %v", gotResult, tt.wantResult)
			}
		})
	}
}
