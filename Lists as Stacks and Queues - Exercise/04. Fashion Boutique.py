from collections import deque

clothes_in_the_box = deque([int(s) for s in input().split()])
capacity = int(input())


def fashion_boutique(cap, clothes):
    c = cap
    racks = 1
    while clothes:
        piese = clothes.popleft()
        if cap - piese >= 0:
            cap -= piese
        else:
            cap = c
            racks += 1
            clothes.appendleft(piese)

    return racks


print(fashion_boutique(capacity, clothes_in_the_box))
