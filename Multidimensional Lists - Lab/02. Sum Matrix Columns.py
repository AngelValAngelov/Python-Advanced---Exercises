row, col = input().split(", ")

matrix = []

for i in range(int(row)):
    new_row = input().split()
    matrix.append(new_row)

for i in range(int(col)):
    s = 0

    for j in range(int(row)):
        s += int(matrix[j][i])

    print(s)
