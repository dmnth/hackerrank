#! /usr/bin/env python3

string = '(({{[]}}))'

middle_idx = len(string) // 2
first_half = []
second_half = []
first_half[0:] = string[:middle_idx]
second_half[0:] = string[middle_idx:]

for i in range(len(first_half)):
	


print(first_half,second_half[::-1])

