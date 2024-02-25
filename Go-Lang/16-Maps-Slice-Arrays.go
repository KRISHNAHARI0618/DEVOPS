package main
import (
	"fmt"
)
func main(){
	// Array Declaration

	var array []int = []int{1,2,3,4,5}
	fmt.Println(array)

	array = append(array,9,10,20)
	fmt.Println(array)

	array1 := array[3]
	fmt.Println(array1)

	//Slice Declaration
	var slice []int = []int{1,2,3,4,5,6,7}
	fmt.Println(slice)

	// Map Declaration

	var my_map map[string]int = map[string]int{"name":1234,"name2":5678}
	fmt.Println(my_map)

}