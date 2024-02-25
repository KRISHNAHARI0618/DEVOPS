package main
import "fmt"

func main()  {
	sum , _:= add(30,20)
	fmt.Println(sum)
	fact := Factorial(5)
	fmt.Println(fact)

	x := func(l int,b int ) int {
		return l * b
	} (20,30)
	fmt.Println(x)
	sum,diff := add(30,20)
	fmt.Println(sum,diff)
}

func add(a int, b int) (int,int){
	sum = a + b
	diff = a - b
	return sum , diff
}

func Factorial(n int) int {
	if n == 1 {
		return 1
	} else {
		return n * Factorial(n-1)
	}
}

// func Veridic(n int ,... int) int {


// }