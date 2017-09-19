package matrix

import (
	"reflect"
	"testing"
)

func TestSpiralOrder(t *testing.T) {
	type args struct {
		m [][]int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
	// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := SpiralOrder(tt.args.m); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("SpiralOrder() = %v, want %v", got, tt.want)
			}
		})
	}
}
