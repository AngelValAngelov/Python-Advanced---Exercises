from collections import deque


def hot_potato(names, number):

    while len(names) != 1:
        for _ in range(1, number):
            n = names.popleft()
            names.append(n)
        print(f"Removed {names.popleft()}")

    print(f"Last is {names[0]}")


hot_potato(names=deque(input().split()), number=int(input()))
