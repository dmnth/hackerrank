somearray = [0, 12, 3, 5, 9, 2, 4]

def sort_array(somearray):

    index = 0
    current_element = somearray[index]

    for i in range(len(somearray)):
        for j in range(i+1, len(somearray)):
            if somearray[i] > somearray[j]:
                element = somearray[i]
                somearray[i] = somearray[j]
                somearray[j] = element

    return somearray
print(sort_array(somearray))