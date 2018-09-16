package mintwosubarraysum

import "testing"

func TestMinTwoSubArraySum(t *testing.T) {
	type args struct {
		elements []int
		s        int
	}
	tests := []struct {
		name          string
		args          args
		wantMinLength int
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if gotMinLength := MinTwoSubArraySum(tt.args.elements, tt.args.s); gotMinLength != tt.wantMinLength {
				t.Errorf("MinTwoSubArraySum() = %v, want %v", gotMinLength, tt.wantMinLength)
			}
		})
	}
}
