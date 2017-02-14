package main

import(
    "fmt"
    "math/rand"
    ) 

func main() {
    fmt.Printf("Enter the size of the random vector: \n")
    var N int
    fmt.Scan(&N)
    
    var list []int

    for index, _ := range list { 
        list[index] = rand.Intn(N)
    }
    fmt.Printf("arr: %v\n", list) 
}
