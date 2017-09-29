package pattern

import (
	"reflect"
	"testing"
)

func Test_generate(t *testing.T) {
	type args struct {
		base []int
	}
	tests := []struct {
		name string
		args args
	}{
		{
			name: "OK",
			args: args{
				base: []int{},
			},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			generate(tt.args.base)
		})
	}
}

func Test_count(t *testing.T) {
	tests := []struct {
		name        string
		wantLengths []int
		wantTotal   int
	}{
		{
			name:        "OK",
			wantLengths: []int{0, 0, 0, 0, 1624, 7152, 26016, 72912, 140704, 140704},
			wantTotal:   389112,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			gotLengths, gotTotal := count()
			if !reflect.DeepEqual(gotLengths, tt.wantLengths) {
				t.Errorf("count() gotLengths = %v, want %v", gotLengths, tt.wantLengths)
			}
			if gotTotal != tt.wantTotal {
				t.Errorf("count() gotTotal = %v, want %v", gotTotal, tt.wantTotal)
			}
		})
	}
}

func Test_sum(t *testing.T) {
	type args struct {
		arr []int
	}
	tests := []struct {
		name  string
		args  args
		wantS int
	}{
		{
			name: "OK",
			args: args{
				arr: []int{1, 2, 3, 4},
			},
			wantS: 10,
		}, {
			name: "OK",
			args: args{
				arr: []int{5, 2, 12, 54},
			},
			wantS: 73,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if gotS := sum(tt.args.arr); gotS != tt.wantS {
				t.Errorf("sum() = %v, want %v", gotS, tt.wantS)
			}
		})
	}
}

func Test_contains(t *testing.T) {
	type args struct {
		i     int
		items []int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "Yes",
			args: args{
				items: []int{1, 2, 3, 4, 5},
				i:     3,
			},
			want: true,
		}, {
			name: "No",
			args: args{
				items: []int{1, 2, 3, 4, 5},
				i:     12,
			},
			want: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := contains(tt.args.i, tt.args.items); got != tt.want {
				t.Errorf("contains() = %v, want %v", got, tt.want)
			}
		})
	}
}
