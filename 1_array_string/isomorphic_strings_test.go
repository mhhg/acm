package strings

import "testing"

func TestIsIsomorphic(t *testing.T) {
	type args struct {
		s string
		t string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
	// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := IsIsomorphic(tt.args.s, tt.args.t); got != tt.want {
				t.Errorf("IsIsomorphic() = %v, want %v", got, tt.want)
			}
		})
	}
}
