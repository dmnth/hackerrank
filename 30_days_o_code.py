# Enter your code here. Read input from STDIN. Print output to STDOUT

returned = input().split(' ')
due = input().split(' ')


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
        return current_fine
    
    if month_returned > month_due and year_returned >= year_due:
        current_fine += (month_returned - month_due) * 500
        return current_fine
    
    if day_returned > day_due and year_returned >= year_due:
        current_fine += (day_returned - day_due) * 15
        return current_fine
    
    else:
        return current_fine

print(fine(returned, due))
    