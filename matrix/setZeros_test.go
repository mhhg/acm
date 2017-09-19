package matrix

import "testing"

func TestSetZeros(t *testing.T) {
	type args struct {
		m [][]int
	}
	tests := []struct {
		name string
		args args
	}{
	// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			SetZeros(tt.args.m)
		})
	}
}
