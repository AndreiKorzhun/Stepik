# create a matrix
matrix = []

# start the loop until the user enters the word 'end'
while True:
    # asks the user for the values of the matrix
    row = input().split()
    if row == ['end']:
        break
    # add the entered values to the matrix and return integers
    matrix.append(list(map(int, row)))

# matrix size
x, y = len(matrix[0]), len(matrix)

# matrix filled with zeros equal in size to the matrix of user values
matrix_sum = [[0 for j in range(x)] for i in range(y)]

# iterate over all matrix values
for i in range(y):
    for j in range(x):
        # each element is equal to the sum of matrix elements at positions
        # (i-1, j), (i+1, j), (i, j-1), (i, j+1)
        matrix_sum[i][j] = matrix[i - 1][j] + matrix[i + 1 - y][j] + \
            matrix[i][j - 1] + matrix[i][j + 1 - x]

# output of all matrix values
for i in range(y):
    print(*matrix_sum[i])
