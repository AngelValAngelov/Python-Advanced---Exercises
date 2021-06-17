rows = int(input())

matrix = [map(int, input().split(", ")) for x in range(rows)]
even_numbers = [[x for x in row if x % 2 == 0] for row in matrix]

print(even_numbers)
