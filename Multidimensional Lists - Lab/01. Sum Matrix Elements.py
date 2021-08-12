row, col = input().split(", ")


matrix = []
summ = 0

for i in range(int(row)):
    new_row = input().split(", ")
    new_row = [int(x) for x in new_row]
    summ += sum(new_row)
    matrix.append(new_row)

print(summ)
print(matrix)