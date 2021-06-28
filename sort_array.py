matrix = [[0, 1, 2],
          [3, 4, 5],
          [6, 7, 8]]

def diagonal_sums(matrix):
    left_sum = 0
    right_sum = 0
    for element in matrix:
        for i in range(len(element)-2):
            print(element[i], element[i+1], element[i+2])
