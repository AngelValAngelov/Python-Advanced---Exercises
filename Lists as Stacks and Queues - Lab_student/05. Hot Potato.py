from collections import deque

peoples = deque(input().split(" "))

number = int(input())

while len(peoples) != 1:
    for people in range(1, number):
        name = peoples.popleft()
        peoples.append(name)
    print(f"Removed {peoples.popleft()}")

print(f"Last is {peoples.popleft()}")









