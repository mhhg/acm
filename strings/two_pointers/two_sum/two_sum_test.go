package twosum

import (
	"reflect"
	"testing"
)

func TestTwoSum(t *testing.T) {
	type args struct {
		numbers []int
		target  int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{
			name: "OK1",
			args: args{
				numbers: []int{2, 7, 11, 15},
				target:  9,
			},
			want: []int{0, 1},
		},
		{
			name: "OK2",
			args: args{
				numbers: []int{2, 7, 11, 15},
				target:  13,
			},
			want: []int{0, 2},
		},
		{
			name: "OK3",
			args: args{
				numbers: []int{43, 21, 131, 815, 475, 12},
				target:  143,
			},
			want: []int{2, 5},
		},
		{
			name: "Failure",
			args: args{
				numbers: []int{4, 7, 11, 15},
				target:  9,
			},
			want: nil,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := TwoSum(tt.args.numbers, tt.args.target); !reflect.DeepEqual(
				got, tt.want) {
				t.Errorf("TwoSum() = %v, want %v", got, tt.want)
			}
		})
	}
}
