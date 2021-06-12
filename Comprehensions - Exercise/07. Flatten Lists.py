numbers = input()

result = [x for x in numbers.split("|")[::-1] for x in x.split(" ") if x != ""]
print(' '.join(result))