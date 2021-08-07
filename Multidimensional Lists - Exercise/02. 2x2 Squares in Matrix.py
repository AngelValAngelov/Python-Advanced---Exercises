rows, cols = input().split()

matrix = []
counter = 0

for _ in range(int(rows)):
    row = input().split()
    matrix.append(row)

for row in range(int(rows) - 1):
    for col in range(int(cols) - 1):
        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            counter += 1


print(counter)
