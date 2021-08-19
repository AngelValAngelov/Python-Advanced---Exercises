number = int(input())

all_elements = set()

for i in range(number):
    elements = input().split()
    for j in elements:
        all_elements.add(j)

for element in all_elements:
    print(element)