package main

import (
	"fmt"
	"strconv"
)

func main() {
	var age string = "23"
	i, j := strconv.Atoi(age)
	fmt.Println(i, j)

	str := "42"
	i, err := strconv.Atoi(str)
	if err != nil {
		fmt.Println("Conversion error:", err)
		return
	} else {
		fmt.Println("My Name is Peddireddy")
	}
	fmt.Println(i)
}
