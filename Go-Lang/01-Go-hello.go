package main

import (
	"fmt"
)

func main() {
	fmt.Println("Congratulations you just Ran Go programming Language")

	var n int = 345
	var s string = "Hello World"
	var b bool = false
	var f float64 = 77.90

	fmt.Println(n)
	fmt.Println(s)
	fmt.Println(b)
	fmt.Println(f)

	var name string = "Hello Mister"
	var user string = "I am Busy"
	fmt.Println("Hey There", name, user)
	fmt.Println("Hey There \n ", name, "\n", user, "\n")

	name2 := "Good Morning"
	fmt.Printf("Hey Guys: %s", name2)

	var syllabus string
	fmt.Println("Enter Your Name:  ")
	fmt.Scanf("%s", &syllabus)
	fmt.Println(syllabus)
}
