package main

import "fmt"

// Structs is like a dictionaries in any other language
// it is like just a key value pairs
type Student struct {
	name string
	rollNo int
}
func main() {

	st := Student{
		name: "Peddireddy",
		rollNo: 1234,
	}
	fmt.Printf("%+v",st)

}