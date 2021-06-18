matrix = [[0, 1, 2],
          [3, 4, 5],
          [6, 7, 8]]

def diagonal_sums(matrix):
    left_sum = 0
    right_sum = 0
    for j in range(len(matrix)):
        left_sum += matrix[j][j]
        right_sum += matrix[j][len(matrix)-j-1]
        

    return left_sum, right_sum

result = diagonal_sums(matrix)
print(result)

