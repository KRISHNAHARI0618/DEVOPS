package main

import (
	"fmt"
)

func main( ) {
	var number int = 10

	switch number {
	case 10:
		fmt.Println("The number is 10")
	case 100,200:
		fmt.Println("The number is 200")
	default:
		fmt.Println("The Number is 100,200")
	}
}