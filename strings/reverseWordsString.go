package strings

/*
ReverseWords Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".
*/
func ReverseWords(str string) string {
	result := ""
	j := 0
	for i, ch := range str {
		if ch == ' ' {
			if j != 0 {
				result = str[j:i] + " " + result
			} else {
				result = str[j:i]
			}
			j = i + 1
		}
	}
	result = str[j:] + " " + result
	return result
}
