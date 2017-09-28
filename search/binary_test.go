package search

import "testing"

func TestBinarySearch(t *testing.T) {
	type args struct {
		list  []int
		value int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "OK",
			args: args{
				list:  []int{1, 2, 3, 4, 5, 6, 7},
				value: 5,
			},
			want: 4,
		}}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := BinarySearch(tt.args.list, tt.args.value); got != tt.want {
				t.Errorf("BinarySearch() = %v, want %v", got, tt.want)
			}
		})
	}
}
