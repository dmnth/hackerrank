#! /usr/bin/env python3

# Grading 

import random

def grading(grades):


	for i in range(len(grades)):
		print(grades[i])
		if grades[i] < 38:
			pass

		else:
			current_grade = grades[i]

			while current_grade % 5 != 0:
				current_grade += 1

			if current_grade - grades[i] < 3:
				grades[i] = current_grade

	return grades
if __name__ == "__main__":

	# Threat those college women with respect:
	grades = [random.randint(0, x) for x in range(0,100)]

	result = grading(grades)
	print(len(result))
