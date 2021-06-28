# plusMinus function

arr = [1, 1, 0, -1, -1]

def plusMinus(arr):
    print(arr)
    zeros = arr.count(0)
    ones = arr.count(1)
    negatives = arr.count(-1)

    zeros_ratio = zero // len(arr)
    ones_ratio = ones // len(arr)
    negatives_ratio = negatives // len(arr)

    return zeros_ratio, ones_ratio, negatives_ratio

print(plusMinus(arr))