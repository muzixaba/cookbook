package main

import ("fmt")

type Employee struct {
    name string
    age int
    isRemote bool
}

func main() {
    employee1 := Employee{
        name: "Muzi",
        age: 38,
        isRemote: true,
    }

fmt.Println("Employee Name: ", employee1.name)

    job := struct {
        title string
        salary int
    }{
        title: "Software Dev",
        salary: 12000,
    }

    fmt.Printf("The %v earns %v \n", job.title, job.salary)

}



