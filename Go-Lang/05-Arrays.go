package main

import (
	"fmt"
	"reflect"
)

func main() {
	var grades [5]int
	fmt.Println(grades)

	grades[0] = 100
	grades[1] = 200
	grades[2] = 300
	grades[3] = 400
	grades[4] = 500

	fmt.Println(grades)

	add()
	arrayInit()
	arrayInit1()
	stringInit()
	MultiDime()

}

func add() {

	var a int = 200
	var b int = 300
	var c int = a + b

	fmt.Println(c)

}

func arrayInit() {

	var grade [3]int = [3]int{10, 20, 30}
	fmt.Println(grade)

}

func arrayInit1() {
	gradess := [4]int{20, 40, 60, 80}
	fmt.Println(gradess)
}

func stringInit() {
	fruits := [4]string{"apples", "bananas", "Grapes", "oranges"}
	fmt.Println(fruits)

	fmt.Println(reflect.TypeOf(fruits))
}

func MultiDime() {

	arrays1 := [3][3]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
	fmt.Println(arrays1)
}
