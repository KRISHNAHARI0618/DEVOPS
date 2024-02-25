package main
import "fmt"

func main(){
	x := func(a int,b int)(int) {
		return a * b
	}(20,50)

	fmt.Printf(" %T ", x)
	fmt.Println(x)
}

