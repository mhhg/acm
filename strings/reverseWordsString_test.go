package strings

import "testing"

func TestReverseWords(t *testing.T) {
	type args struct {
		str string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
	// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := ReverseWords(tt.args.str); got != tt.want {
				t.Errorf("ReverseWords() = %v, want %v", got, tt.want)
			}
		})
	}
}
