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
	}{{
		name: "OK",
		args: args{
			str: "the sky is blue",
		},
		want: "blue is sky the",
	}, {
		name: "OK2",
		args: args{
			str: "this is test reverse words func on strings package",
		},
		want: "package strings on func words reverse test is this",
	}}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := ReverseWords(tt.args.str); got != tt.want {
				t.Errorf("ReverseWords() = %v, want %v", got, tt.want)
			}
		})
	}
}
