package main

import "fmt"

func main(){
	s := "Hello"
	var s_ptr *string = &s
	fmt.Println(s_ptr)

	n := "People"
	var n_ptr = &n
	fmt.Println(n_ptr)

	t := "Doing"
	t_ptr := &t
	fmt.Println(t_ptr)
}