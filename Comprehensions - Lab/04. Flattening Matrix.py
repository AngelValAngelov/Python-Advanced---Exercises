rows = int(input())

matrix = [map(int, input().split(", ")) for x in range(rows)]
flatten = [x for x in matrix for x in x]

print(flatten)