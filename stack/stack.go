package stack

/*
The requirements of the stack are:
	1) the stack has a constructor which accept a number to initialize its size,
	2) the stack can hold any type of elements
	3) the stack has a push() and a pop() method.
*/
type Stack interface {
	Pop()
	Push()
	String()
}
