lenght_set_1, lenght_set_2 = list(map(int, input().split()))

set_1 = set()
set_2 = set()
for i in range(lenght_set_1):
    number = input()
    set_1.add(number)

for i in range(lenght_set_2):
    number = input()
    set_2.add(number)

all_numbers_in_sets = set_1 & set_2

for number in all_numbers_in_sets:
    print(number)