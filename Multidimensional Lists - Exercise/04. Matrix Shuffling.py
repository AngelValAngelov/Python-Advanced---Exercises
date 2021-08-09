rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    row = [x for x in input().split()]
    matrix.append(row)

while True:
    command = [x for x in input().split()]
    if command[0] == "END":
        break
    if len(command) == 5:
        action = command[0]
        row_1 = int(command[1])
        col_1 = int(command[2])
        row_2 = int(command[3])
        col_2 = int(command[4])
    else:
        print("Invalid input!")
        continue
    if command[0] == "swap":
        if row_1 > rows and col_1 > cols and row_2 > rows and col_2 > cols:
            print("Invalid input!")
            continue
        else:
            matrix_first_row = matrix[row_1][col_1]
            matrix[row_1][col_1] = matrix[row_2][col_2]
            matrix[row_2][col_2] = matrix_first_row
            for row in range(rows):
                print(" ".join([x for x in matrix[row]]))
    else:
        print("Invalid input!")







