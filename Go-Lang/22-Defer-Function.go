package main

import "fmt"

func main(){
	defer studentName("Peddireddy")
	defer studentAddress("Chiyyapadu")
	studentRollNo(45)

}

func studentName(name string) {
	fmt.Println(name)
}
func studentRollNo(number int) {
	fmt.Println(number)
}
func studentAddress(address string){
	fmt.Println(address)
}