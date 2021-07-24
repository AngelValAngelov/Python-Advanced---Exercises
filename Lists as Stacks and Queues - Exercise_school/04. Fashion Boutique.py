clothes = [int(x) for x in input().split()]
capacity = int(input())
number = 1
r_cap = capacity
while clothes:
    if r_cap - clothes[-1] > 0:
        r_cap -= clothes[-1]
        clothes.pop()
    elif r_cap - clothes[-1] == 0:
        r_cap = capacity
        if len(clothes) != 1:
            number += 1
        clothes.pop()
    else:
        r_cap = capacity
        number += 1
print(number)

