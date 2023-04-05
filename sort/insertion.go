package sort

import (
	"fmt"
	"reflect"
	"testing"
)

// InsertionSort o(n2)
func InsertionSort(list []int) []int {
	for i := 1; i < len(list); i++ {
	
		if list[i] < list[i-1] {
			tmp := list[i-1]
			list[i-1] = list[i]
			list[i] = tmp
	
			for j := i - 1; j > 0; j-- {
				if list[j] < list[j-1] {
					tmp := list[j-1]
					list[j-1] = list[j]
					list[j] = tmp
				}
			}
		}
	}

	return list
}


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

// Runs MergeSort algorithm on a slice single
func MergeSort(slice []int) []int {

	if len(slice) < 2 {
		return slice
	}
	mid := (len(slice)) / 2
	return Merge(MergeSort(slice[:mid]), MergeSort(slice[mid:]))
}

// Merges left and right slice into newly created slice
func Merge(left, right []int) []int {

	size, i, j := len(left)+len(right), 0, 0
	slice := make([]int, size, size)

	for k := 0; k < size; k++ {
		if i > len(left)-1 && j <= len(right)-1 {
			slice[k] = right[j]
			j++
		} else if j > len(right)-1 && i <= len(left)-1 {
			slice[k] = left[i]
			i++
		} else if left[i] < right[j] {
			slice[k] = left[i]
			i++
		} else {
			slice[k] = right[j]
			j++
		}
	}
	return slice
}