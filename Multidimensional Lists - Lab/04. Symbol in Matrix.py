number = int(input())

matrix = [input() for _ in range(number)]

symbol = input()


def solve(matrix, symbol):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == symbol:
                return (row, col)
    return None


result = solve(matrix, symbol)
if result:
    (row, col) = result
    print(f"({row}, {col})")
else:
    print(f"{symbol} does not occur in the matrix")
