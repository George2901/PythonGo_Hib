package main

import "C"

//export Print
func Print(input *C.char) *C.char {
	inputString := C.GoString(input)

	outputString := "Hello " + inputString

	println(inputString)

	return C.CString(outputString)
}

func main() {}
