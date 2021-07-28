from collections import deque


def water_dispenser():
    litters = int(input())
    names = deque()
    while True:
        name = input()
        if name != "Start":
            names.append(name)
        else:
            break

    while True:
        water = input().split()
        if water[0] == "End":
            print(f"{litters} liters left")
            break
        elif water[0] == "refill":
            litters += int(water[1])
        elif litters - int(water[0]) >= 0:
            litters -= int(water[0])
            print(f"{names.popleft()} got water")
        else:
            print(f"{names.popleft()} must wait")


water_dispenser()