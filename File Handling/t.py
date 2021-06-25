file_path = '../file/File Opener/text.txt'

file = open(file_path, "r")

index = 0
for line in file:
    print(f'{index}: {line}')
    index += 1
