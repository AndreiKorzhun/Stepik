# specifies the size of the matrix
n = int(input())

matrix = [[0 for j in range(n)] for i in range(n)]
# matrix size indices
x, y = 0, n - 1
# the number to fit into the matrix
i = 1

while i <= n ** 2:
    # fills the matrix from left to right with the number i
    for j in range(x, y):
        matrix[x][j] += i
        i += 1

    # fills the matrix from top to bottom with the number i
    for j in range(x, y):
        matrix[j][y] += i
        i += 1

    # fills the matrix from right to left with the number i
    for j in range(y, x, - 1):
        matrix[y][j] += i
        i += 1

    # fills the matrix from bottom to top with the number i
    for j in range(y, x, -1):
        matrix[j][x] += i
        i += 1

    # inserts the number in the center of the matrix if the matrix is odd size
    if n % 2 != 0 and i == n ** 2:
        matrix[n // 2][n // 2] += i
        i += 1

    # after each round-trip, decrements the matrix size indices
    x += 1
    y -= 1

for row in matrix:
    print(*row)
