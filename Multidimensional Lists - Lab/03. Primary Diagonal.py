rows_count = int(input())

summ = 0

for i in range(rows_count):
    row = input().split()
    summ += int(row[i])

print(summ)