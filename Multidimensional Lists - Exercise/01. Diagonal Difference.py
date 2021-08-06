matrix_size = int(input())

matrix = []

for _ in range(matrix_size):
    row = input().split()
    matrix.append([int(x) for x in row])

primary_diagonal_sum = 0
secondary_diagonal_sum = 0

for i in range(matrix_size):
    primary_diagonal_sum += matrix[i][i]
    secondary_diagonal_sum += matrix[i][-i - 1]

difference = abs(primary_diagonal_sum - secondary_diagonal_sum)

print(difference)