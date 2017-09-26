package sort

import (
	"fmt"
	"reflect"
	"testing"
)

func TestInsertionSort(t *testing.T) {
	type args struct {
		list []int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{{
		name: "OK",
		args: args{
			[]int{4, 2, 6, 3},
		},
		want: []int{2, 3, 4, 6},
	}, {
		name: "OK2",
		args: args{
			[]int{90, 70},
		},
		want: []int{70, 90},
	}, {
		name: "OK3",
		args: args{
			[]int{134, 90, 56, 34, 64, 12, 4, 0, 1, 43, 23, 0, 34, 0, 25, 54, 65},
		},
		want: []int{0, 0, 0, 1, 4, 12, 23, 25, 34, 34, 43, 54, 56, 64, 65, 90, 134},
	}}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := InsertionSort(tt.args.list)
			fmt.Println(got)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("InsertionSort() = %v, want %v", got, tt.want)
			}
		})
	}
}
