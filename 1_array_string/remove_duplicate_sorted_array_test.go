package strings

import (
	"reflect"
	"testing"
)

func TestRemoveDuplicate1(t *testing.T) {
	type args struct {
		arr []int
	}
	tests := []struct {
		name  string
		args  args
		want  int
		want1 []int
	}{
		{
			name: "OK",
			args: args{
				arr: []int{1, 1, 2},
			},
			want:  2,
			want1: []int{1, 2},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, got1 := RemoveDuplicate1(tt.args.arr)
			if got != tt.want {
				t.Errorf("RemoveDuplicate1() got = %v, want %v", got, tt.want)
			}
			if !reflect.DeepEqual(got1, tt.want1) {
				t.Errorf("RemoveDuplicate1() got1 = %v, want %v", got1, tt.want1)
			}
		})
	}
}
