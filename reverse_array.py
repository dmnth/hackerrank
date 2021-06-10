#! /usr/bin/env python3

# Reverse array

def reverse_array(var):
	
	size = len(var)
	last_index = size - 1
	itrs = size // 2

	for i in range(len(var)):

		temp = var[i]
		var[i] = var[last_index]
		var[last_index] = temp

		last_index -= 1

	return var
