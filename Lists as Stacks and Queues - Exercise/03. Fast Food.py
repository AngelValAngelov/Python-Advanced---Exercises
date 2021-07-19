from collections import deque

number = int(input())
nums = [int(x) for x in input().split()]


def fast_food(n, ns):
    is_true = True
    s = list()
    left = deque()
    max_num = max(ns)
    for i in ns:
        if n >= int(i) and is_true:
            s.append(int(i))
            n -= int(i)
        else:
            left.append(int(i))
            is_true = False
    if left:
        print(max_num)
        print(f"Orders left: {' '.join(str(x) for x in left)}")
    else:
        print(max_num)
        print("Orders complete")


fast_food(number, nums)



