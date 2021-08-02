from collections import deque


def litters_up(current_litters, refill):
    current_litters += refill
    return current_litters


def litters_down(current_litters, empty):
    current_litters -= empty
    return current_litters


litters = int(input())
deque = deque()

while True:
    name = input()
    if name == "Start":
        break
    else:
        deque.append(name)

current_water = litters

while True:
    water = input()
    if water == "End":
        print(f"{current_water} liters left")
        break
    if water[0].isnumeric():
        if litters_down(int(current_water), int(water)) >= 0:
            current_water = litters_down(int(current_water), int(water))
            print(f"{deque.popleft()} got water")
        else:
            print(f"{deque.popleft()} must wait")
    else:
        water = water.split()
        current_water = litters_up(int(current_water), int(water[1]))
