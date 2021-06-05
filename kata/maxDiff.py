#! /usr/bin/env python3

# Function checks each element in array and finds
# maximum difference between any two elements

def maxDiff(somelist):

    somelist.sort(reverse=True)


    print(somelist[0] - somelist[-1])
if __name__ == "__main__":
    maxDiff([1, 2, 5, 4, 0, 3])
