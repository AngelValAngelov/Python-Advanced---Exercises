from collections import deque

stops = int(input())

all_stops = deque()

for _ in range(stops):
    pump = [int(x) for x in input().split()]
    all_stops.append([int(x) for x in pump])

temporary_stops = all_stops

number = -1
temporary_liters = 0
last_stops = all_stops
for _ in range(stops):
    if not temporary_stops:
        break
    number += 1
    while last_stops:
        liters, kilometers = temporary_stops[0]
        temporary_liters += int(liters)
        if int(temporary_liters) >= int(kilometers):
            temporary_liters -= int(kilometers)
            s = temporary_stops.popleft()
            last_stops.append(s)
            last_stops.popleft()
        else:
            temporary_stops.append(temporary_stops[0])
            temporary_stops.popleft()
            temporary_liters = 0
            number = 0
            break


print(number)

