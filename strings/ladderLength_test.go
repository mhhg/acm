package strings

import "testing"

func TestLadderLength(t *testing.T) {
	type args struct {
		begin   string
		end     string
		wordDit wordNode
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
			if got := LadderLength(tt.args.begin, tt.args.end, tt.args.wordDit); got != tt.want {
				t.Errorf("LadderLength() = %v, want %v", got, tt.want)
			}
		})
	}
}
