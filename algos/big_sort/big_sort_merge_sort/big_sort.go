package main

import (
	"fmt"
	"math/big"
)

func main() {

	collection := []string{"34", "12", "76", "0", "12303479849857341718340192371", "75", "-1"}
	fmt.Println(collection)
	result := merge_sort(collection)
	fmt.Println(result)

}

// Function takes an array of str(number)
// Returns sorted array in same format
// ['1', '200', '150', '3'] ---> ['1', '3', '150', '200']

//! Works but fails due timeout on hackkerank

func merge_sort(someArr []string) []string {

	if len(someArr) < 2 {
		return someArr
	}

	var midIdx int = len(someArr) / 2

	var left_split []string = someArr[:midIdx]
	var right_split []string = someArr[midIdx:]

	var left_sorted []string = merge_sort(left_split)
	var right_sorted []string = merge_sort(right_split)

	return merge(left_sorted, right_sorted)
}

func merge(left []string, right []string) []string {

	var result []string
	// Dont forget to add base, 10 for now, up to 62

	for {

		left_elem, ok := new(big.Int).SetString(left[0], 10)
		right_elem, ok := new(big.Int).SetString(right[0], 10)

		if ok == false {
			panic(ok)
		}

		if left_elem.Cmp(right_elem) == -1 {
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
		result = append(result, left...)
	}

	if len(right) > 0 {
		result = append(result, right...)
	}

	return result
}
