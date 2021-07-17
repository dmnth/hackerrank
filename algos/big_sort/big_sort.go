package main

import (
	"fmt"
	"strconv"
)

func main() {

	collection := []string{"34", "12", "76", "0", "92", "75"}
	fmt.Println(collection)
	convert(collection)
	result := merge_sort(collection)
	fmt.Println(result)

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

	//	fmt.Printf("left split: %s\nright split: %s\n", left_split, right_split)
	//	fmt.Println(left_sorted, right_sorted)

	return merge(left_sorted, right_sorted)
}

func merge(left []string, right []string) []string {

	var result []string

	for {
		// Use parseint instead of atoi with byte-size modified as 10 64
		left_elem, err := strconv.ParseInt(left[0], 10, 64)
		right_elem, err := strconv.ParseInt(right[0], 10, 64)

		if err != nil {
			panic(err)
		}

		if left_elem < right_elem {
			fmt.Println(left_elem, right_elem)
			result = append(result, left[0])
			// So that is how you pop first item from slice in golang
			left = append(left[:0], left[1:]...)

		} else {

			result = append(result, right[0])
			right = append(right[:0], right[1:]...)

		}

		if len(left) == 0 || len(right) == 0 {
			break
		}
	}

	if len(left) > 0 {
		// Three dots notation --> iteratively append all elements from given
		// slice to target
		fmt.Println(left)
		result = append(result, left...)
	}

	if len(right) > 0 {
		result = append(result, right...)
		fmt.Println(right)
	}

	return result
}
