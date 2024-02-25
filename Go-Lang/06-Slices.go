package main

import (
	"fmt"
)

func main() {
	arrays := []int{2, 3, 4, 5, 6, 7}
	fmt.Println(arrays)

	arrays2 := []int{4, 5, 6, 7, 8, 9, 10, 34, 56}
	fmt.Println(arrays2)

	slice := arrays2[1:5]
	fmt.Println(slice)
	slicef()
	slice_2()
	deletslice()
	looping()
	dec()

}

func slicef() {
	slice := make([]int, 5, 20)
	fmt.Println(cap(slice))
}

func slice_2() {
	slicer := []int{4, 5, 6, 7, 8, 9, 10, 34, 56}
	fmt.Println(slicer)

	slicer1 := slicer[:5]
	fmt.Println(slicer1)

	slicer2 := slicer1[:4]
	fmt.Println(slicer1, slicer2)

	new_slice := append(slicer1, slicer2...)
	fmt.Println(new_slice)

}

func deletslice() {
	slicer3 := []int{4, 5, 6, 7, 8, 9, 10, 34, 56}

	fmt.Println(slicer3)
}

func looping() {
	sli := []int{4, 5, 6, 7, 8, 9, 10, 34, 56}

	for i, v := range sli {
		fmt.Println(i, v)
	}
}

func dec() {
	slis := []int{4, 5, 6, 7, 8, 9, 10, 34, 56}

	fmt.Println(slis)

	dest := make([]int, 4)
	num := copy(dest, slis)

	fmt.Println(dest)
	fmt.Println(num)

}
