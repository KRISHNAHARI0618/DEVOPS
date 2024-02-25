package main

import "fmt"

func main(){
  x1 := highOrderFunction(add,3,4)
	fmt.Println(x1)

	y1 := highOrderFunction(multiply,3,4)
	fmt.Println(y1)
}

func highOrderFunction(f func(int,int) int, a,b int) int {
	return f(a,b)
}

func add(x,y int) int {
	return x+y
}

func multiply(x,y int)int {
	return x * y
}