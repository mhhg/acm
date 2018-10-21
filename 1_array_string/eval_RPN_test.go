package strings

import "testing"

func TestEvalRPN(t *testing.T) {
	type args struct {
		tokens []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
	// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := EvalRPN(tt.args.tokens); got != tt.want {
				t.Errorf("EvalRPN() = %v, want %v", got, tt.want)
			}
		})
	}
}
