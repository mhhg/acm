package strings

import (
	"reflect"
	"testing"
)

func TestFindLadders(t *testing.T) {
	type args struct {
		start string
		end   string
		dict  wordNodes
	}
	tests := []struct {
		name string
		args args
		want [][]string
	}{
	// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := FindLadders(tt.args.start, tt.args.end, tt.args.dict); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("FindLadders() = %v, want %v", got, tt.want)
			}
		})
	}
}
