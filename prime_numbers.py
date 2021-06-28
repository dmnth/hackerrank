somearray = [0, 12, 3, 5, 9, -1]

def sort_array(somearray):

    index = 0
    current_element = somearray[index]

    for i in range(len(somearray)-1):

        if somearray[i] > somearray[i + 1]:

            somearray[i], somearray[i+1] = somearray[i+1], somearray[i]

sort_array(somearray)