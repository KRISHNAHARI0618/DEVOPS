package main
import "fmt"

func main(){
	fmt.Println("Hello World")
	addition,subtraction := add(30,20)
	fmt.Println(addition,subtraction)
	fmt.Println(veridic())
	fmt.Println(veridic(10,20))
	fmt.Println(veridic(20,30,40))
	PrintDetails("Joe","Physics","Biology","Science")

	a,_ := f()
	fmt.Println(a)
}

func add(a int , b int) (sum int, difference int){
	sum = a + b
	difference = a - b
	return sum,difference
}

func veridic(numbers ...int) int{
	sum := 0
	for _,value := range numbers{
		sum = sum + value
	}
	return sum
}

func PrintDetails(student string, subjects ...string) {
	fmt.Println("hey",student,", here are your students - ")
	for _,sub := range subjects{
		fmt.Printf("%s ,", sub)
	}
}

func f() (int,int){
	return 42,56
}