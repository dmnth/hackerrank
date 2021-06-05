#! /usr/bin/env python3

def max_difference(somearray):

    result = []

    for element in somearray:
        for j in range(len(somearray) -1 ):
            result.append(abs(element-somearray[j])) 

    print(result)
    return max(result)


if __name__ == "__main__":
    somearray = [7, 7, 6]
    result = max_difference(somearray)
    print(result)

