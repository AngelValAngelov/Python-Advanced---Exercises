rows, cols = input().split()

matrix = []

for _ in range(int(rows)):
    row = input().split()
    matrix.append([int(x) for x in row])
summ = 0
final_square = []

for row in range(int(rows) - 2):
    for col in range(int(cols) - 2):
        square_sum = matrix[row][col] + matrix[row][col+ 1] + matrix[row][col + 2]\
                     + matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2]\
                     + matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
        if square_sum > summ:
            summ = square_sum
            final_square = [[matrix[row][col], matrix[row][col+ 1], matrix[row][col + 2]]
                , [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]]
                , [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]]


print(f"Sum = {summ}")

print(f"{final_square[0][0]} {final_square[0][1]} {final_square[0][2]}")
print(f"{final_square[1][0]} {final_square[1][1]} {final_square[1][2]}")
print(f"{final_square[2][0]} {final_square[2][1]} {final_square[2][2]}")