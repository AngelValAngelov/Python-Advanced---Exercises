rows = int(input())
matrix = [[int(x) for x in input().split(", ")] for x in range(rows)]

first = [matrix[x][x] for x in range(rows)]
second = [matrix[x][-x - 1] for x in range(rows)]

print(f"First diagonal: {', '.join(str(x) for x in first)}. Sum: {sum(first)}")
print(f"Second diagonal: {', '.join(str(x) for x in second)}. Sum: {sum(second)}")