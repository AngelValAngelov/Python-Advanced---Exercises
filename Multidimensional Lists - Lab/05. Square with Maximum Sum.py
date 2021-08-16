rows,cols = input().split(", ")

matrix = []

for _ in range(int(rows)):
    new_row = input().split(", ")
    matrix.append([int(x) for x in new_row])

row_1 = 0
row_2 = 0
col_1 = 0
col_2 = 0
summ = 0


for row in range(int(rows) - 1):
    for col in range(int(cols) - 1):
        if int(matrix[row][col]) + int(matrix[row][col + 1]) + int(matrix[row + 1][col]) + int(matrix[row + 1][col + 1]) > summ:
            summ = int(matrix[row][col]) + int(matrix[row][col + 1]) + int(matrix[row + 1][col]) + int(matrix[row + 1][col + 1])
            row_1, row_2, col_1, col_2 = int(matrix[row][col]), int(matrix[row][col + 1]), int(matrix[row + 1][col]), int(matrix[row + 1][col + 1])

print(f"{row_1} {row_2}\n{col_1} {col_2}")
print(summ)