file_path = '../file/File Reader/numbers.txt'

file = open(file_path , "r")

summ = 0

for n in file:
    summ += int(n)

print(summ)