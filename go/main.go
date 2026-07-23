package main //every Go file starts with package. All Go files are part of a package

import (
	"errors"
	"fmt"
    "time"
) // importing the built-in Format package for its Print function
// Go doesn't allow you to import and not use packages.

// globally scoped variables are declared at the top of the file
var globalVar string = "I'm a global variable"

// There are no Classes in Go. 
// Use structs with the behavior in a receiver function
type User struct {
	ID   int
	Name string
}

// Greet is a method. The (u User) is the "receiver", similar to 'self' in python
func (u User) Greet() (string, error) {
	return "Hi, my name is " + u.Name, nil
}

// divide is a function that returns a quotient from 2 numbers
func divide(a, b float64) (float64, error) {
	if b == 0 {
		return 0, errors.New("Can't divide by 0")
	}
	return a / b, nil
}

func main() {
	fmt.Print("Hello go world \n")
	fmt.Print("This is a string \n")
	fmt.Println("Println add a new line at the end")
	fmt.Println() //print empty line
	fmt.Println(5)

	// Primitives
	fmt.Print("This is a string")
	fmt.Print("Inters include int, int32, int64, uint")
	fmt.Print("Floating Points include float32 and float64 (default)")
	fmt.Print("Booleans are true and false")

	// Variables
	var x int = 10
	y := 5 // short hand variable declaration (function scoped variables ONLY)

	fmt.Println(globalVar)

    fmt.Println(x == y) // checking for equality
    fmt.Println(x != y)
    
    var floatee float64 = 13342.33
    fmt.Println(floatee)

    var goIsFast bool = true
    fmt.Println(goIsFast)

    const myConst string = "You can't change the value of a constant"
    fmt.Println(myConst)

	// Default variables
	var k int = 0
    fmt.Println(k)

	//defaultString := ""
    var defaultBool = false
    fmt.Println(defaultBool)

	// Pointers & Slices are Nil

	// Using the User struct
	u := User{ID: 1, Name: "Muzi"}
	greeting, err := u.Greet()
	if err != nil {
		fmt.Println("Error:", err)
	}
	fmt.Println(greeting)

	//Slices are similar to Python Lists
	s := []int{1, 2, 3}
	s = append(s, 4)
	fmt.Println(s)

	//Maps are similar to Python dicts
	d := make(map[string]int)
	d["key"] = 43
	fmt.Println(d)

	// Calling the divide function
	res, err := divide(10, 0)
	if err != nil {
	fmt.Println("Error:", err)
		return
	}
	fmt.Println("Result:", res)
    fmt.Printf("Using Printf for easy formating: Result = %v", res)

    //If statements
    if  1 == 1 && 2 == 2{
        fmt.Println("All all true")
    } else {
        fmt.Println("Not equal")
    }

    //Switch statements
    dayOfWeek := time.Now().Weekday()
    switch dayOfWeek {
    case time.Saturday:
        fmt.Println("Today is Saturday")
    case time.Sunday:
        fmt.Println("Today is Sunday")
    default:
        fmt.Println("Today is a weekday")
    }
}
