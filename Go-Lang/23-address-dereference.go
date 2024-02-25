package main

import "fmt"

func main() {

	i := 20

	// & ampersand refers Address of variable
	// * asterisk refers Pointer of variable

	fmt.Printf("%T, %v \n ", &i,&i)
	fmt.Printf("%T,%v \n ", *(&i),*(&i))

	var ptr *int = &i
	*ptr = 100
	fmt.Printf("%T, %v \n" , *ptr,&(*ptr))

}