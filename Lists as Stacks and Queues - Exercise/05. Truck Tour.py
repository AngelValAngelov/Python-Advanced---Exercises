from collections import deque

value = int(input())
all_stations = list()


def truck_tour(v):
    for _ in range(v):
        station = input().split()
        all_stations.append(station)

    temporary_stations = deque(all_stations)

    result = 0

    while temporary_stations:
        gas_distance = temporary_stations[0]
        gas_amount = int(temporary_stations[0][0])
        distance = int(temporary_stations[0][1])
        if gas_amount < distance:
            temporary_stations.append(gas_distance)
            temporary_stations.popleft()
            result += 1
            continue
        else:
            stations = deque(temporary_stations)
            liters_left = 0
            while stations:
                station_gas = stations[0]
                next_station = int(stations[0][1])
                next_gas = int(stations[0][0])
                if next_gas + liters_left >= next_station:
                    liters_left += next_gas - next_station
                    stations.popleft()
                else:
                    stations = temporary_stations
                    liters_left = 0
                    break
            if not stations:
                break
        temporary_stations.append(gas_distance)
        temporary_stations.popleft()
        result += 1
    return result


print(truck_tour(value))
