file_path = '../Exercise_ File Handling/text.txt'

with open(file_path, 'r') as file:

    counter = 1

    for i in file:
        counter += 1
        if counter % 2 == 0:
            for x in "-,.!?":
                i = i.replace(x, "@")
            i = reversed(i.split())
            print(' '.join(i))