number = int(input())

equal_names = []

for i in range(number):
    equal_names.append(input())

for name in set(equal_names):
    print(name)