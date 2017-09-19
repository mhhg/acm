package strings

type wordNodes struct {
	Word  string
	Steps int
	Pre   *wordNodes
}

/*
FindLadders Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that: 1) Only one letter can be changed at a time, 2) Each intermediate word must exist in the dictionary.

For example, given: start = "hit", end = "cog", and dict = ["hot","dot","dog","lot","log"], return:

  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
*/
func FindLadders(start, end string, dict wordNodes) [][]string {
	return nil
}
