package main

import "fmt"

// highOrderFunc takes a function f and two integers, and applies f to the integers
func highOrderFunc(f func(int, int) int, a, b int) int {
	return f(a, b)
}

// Example functions to be used with highOrderFunc
func add(x, y int) int {
	return x + y
}

func multiply(x, y int) int {
	return x * y
}

func main() {
	// Using highOrderFunc with the add function
	resultAdd := highOrderFunc(add, 3, 4)
	fmt.Printf("Result of addition: %d\n", resultAdd)

	// Using highOrderFunc with the multiply function
	resultMultiply := highOrderFunc(multiply, 3, 4)
	fmt.Printf("Result of multiplication: %d\n", resultMultiply)
}
