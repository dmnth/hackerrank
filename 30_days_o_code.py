#! /usr/bin/env python3

# Enter your code here. Read input from STDIN. Print output to STDOUT

returned = '31122009'
due = '112010'

def fine(returned, due):
    
    fine_per_day = 15
    current_fine = 0
    
    day_returned = int(returned[0])
    month_returned = int(returned[1])
    year_returned = int(returned[2])

    day_due = int(due[0])
    month_due =int(due[1])
    year_due = int(due[2])

    if year_returned > year_due:
    	current_fine += 10000
    	print('year is due')
    	return

    if month_returned > month_due:
    	current_fine += 500 * (month_returned - month_due)
    	print('year is due')
    	return

    if day_returned > day_due and year_returned >= year_due:
    	current_fine += 15 * (day_returned - day_due)
    	print('day is due')
    	print(day_returned, day_due)
    	return

print(fine(returned, due))
