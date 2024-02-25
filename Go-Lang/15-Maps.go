package main

import (
	"fmt"
)

func main(){
	// var my_map map[string] int
	// fmt.Println(my_map)

	my_map := map[string]int{"id1":1234,"id2":5678}
	fmt.Println(my_map)

	map1 := make(map[string]int)
	fmt.Println(map1)

	my_map["id3"] = 3456
	fmt.Println(my_map)

	my_map["id2"] = 9876
	fmt.Println(my_map)
	delete(my_map,"id2")
	fmt.Println(my_map)

	for key,value := range my_map{
		fmt.Println(key,"=",value)
	}

}