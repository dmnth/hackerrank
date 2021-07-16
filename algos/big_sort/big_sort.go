package main

import (
	"fmt"
	"strconv"
)

func main() {

	collection := []string{"12", "34", "676", "0", "12", "76"}
	fmt.Println(collection)
	convert(collection)
	merge_sort(collection)

}

// Function takes an array of str(number)
// Returns sorted array in same format
// ['1', '200', '150', '3'] ---> ['1', '3', '150', '200']

func convert(strArr []string) []int {

	var intArr = make([]int, len(strArr))

	for idx, i := range strArr {
		intElem, err := strconv.Atoi(i)
		//		fmt.Printf("%s: %d at index %d\n", i, intElem, idx)

		if err != nil {
			panic(err)
		}
		intArr[idx] = intElem
	}
	return intArr
}

func merge_sort(someArr []string) []string {

	if len(someArr) <= 1 {
		return someArr
	}

	var midIdx int = len(someArr) / 2

	var left_split []string = someArr[:midIdx]
	var right_split []string = someArr[midIdx:]

	var left_sorted []string = merge_sort(left_split)
	var right_sorted []string = merge_sort(right_split)

	fmt.Printf("left split: %s\nright split: %s\n", left_split, right_split)
	fmt.Println(left_sorted, right_sorted)

	return someArr
}
