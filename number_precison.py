# plusMinus function

_arr = [1, 1, 0, -1, -1]
arr = [-4, 3, -9, 0, 4, 1]

def plusMinus(arr):
    print(arr)
    zeros = arr.count(0)
    ones = arr.count(1)
    negatives = arr.count(-1)

    zeros_ratio = zeros / len(arr)
    ones_ratio = ones / len(arr)
    negatives_ratio = negatives / len(arr)

    print('{:.6f}'.format(zeros_ratio))
    print('{:.6f}'.format(ones_ratio))
    print('{:.6f}'.format(negatives_ratio))

    return zeros_ratio, ones_ratio, negatives_ratio

print(plusMinus(arr))