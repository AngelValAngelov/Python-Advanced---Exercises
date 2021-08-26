number = int(input())

car_on_parking = []
for i in range(number):
    direction, car_number = input().split(", ")
    if direction == "IN":
        if car_number in car_on_parking:
            continue
        else:
            car_on_parking.append(car_number)
    else:
        if car_number in car_on_parking:
            car_on_parking.remove(car_number)
        else:
            continue

if car_on_parking:
    for i in car_on_parking:
        print(i)
else:
        print("Parking Lot is Empty")