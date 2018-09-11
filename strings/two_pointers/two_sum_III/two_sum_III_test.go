package twosum3

import (
	"testing"
)

func TestTwoSum_Add(t *testing.T) {
	type args struct {
		num int
	}
	tests := []struct {
		name string
		ts   *TwoSum
		args args
	}{
		{
			name: "ok",
			ts:   NewTwoSum(1, 3, 5),
			args: args{
				num: 7,
			},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			tt.ts.Add(tt.args.num)
		})
	}
}

func TestTwoSum_Find(t *testing.T) {
	type args struct {
		value int
	}
	tests := []struct {
		name string
		ts   *TwoSum
		args args
		want bool
	}{
		{
			name: "ok",
			ts:   NewTwoSum(1, 3, 5),
			args: args{
				value: 4,
			},
			want: true,
		},
		{
			name: "ok2",
			ts:   NewTwoSum(1, 3, 5),
			args: args{
				value: 6,
			},
			want: true,
		},
		{
			name: "ok3",
			ts:   NewTwoSum(1, 3, 5),
			args: args{
				value: 8,
			},
			want: true,
		},
		{
			name: "duplicate_return_false",
			ts:   NewTwoSum(1, 3, 5),
			args: args{
				value: 2,
			},
			want: false,
		},
		{
			name: "duplicate_return_false2",
			ts:   NewTwoSum(1, 3, 5),
			args: args{
				value: 10,
			},
			want: false,
		},
		{
			name: "should_return_false",
			ts:   NewTwoSum(1, 3, 5),
			args: args{
				value: 7,
			},
			want: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.ts.Find(tt.args.value); got != tt.want {
				t.Errorf("TwoSum.Find() = %v, want %v", got, tt.want)
			}
		})
	}
}
