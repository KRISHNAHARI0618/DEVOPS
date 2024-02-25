package main

import (
	"fmt"
)

func main() {

	// var i  int = 1
	for i := 1; i <= 10; i++ {
		fmt.Println("Hello World")
	}

	for i := 1; i <= 20; i *= 2 {
		fmt.Println(i)
	}

	for i := 10; i < 50; i++ {
		if i%2 == 0 {
			fmt.Println(i)
		} else {
			fmt.Println("Stop The Looping")
		}
	}
}
