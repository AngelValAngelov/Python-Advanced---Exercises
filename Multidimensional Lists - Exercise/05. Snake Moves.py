from collections import deque

rows, cols = [int(x) for x in input().split()]
matrix = [["" for x in range(cols)] for y in range(rows)]
text = deque([x for x in input()])

for i in range(rows):
    for j in range(cols):
        if i % 2 == 0:
            char = text.popleft()
            matrix[i][j] = char
            text.append(char)
        else:
            char = text.popleft()
            matrix[i][-j - 1] = char
            text.append(char)

for i in range(rows):
    print("".join(matrix[i]))
