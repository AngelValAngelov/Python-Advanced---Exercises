from collections import deque


def current_time(h, m, s):
    s += 1
    if s == 60:
        s = 0
        m += 1
    if m == 60:
        m = 0
        h += 1
    if h == 24:
        h = 0
    temporary_time = [h, m, s]
    return temporary_time


def robotics():
    available_robots = deque()
    working_robots = list()
    robots_time = [x for x in input().replace("-", " ").replace(";", " ").split()]
    time = [int(x) for x in input().split(":")]
    items = deque()
    robots = {}

    for i in range(len(robots_time)):
        if i % 2 == 0:
            robots[robots_time[i]] = robots_time[i + 1]
            available_robots.append(robots_time[i])

    while True:
        item = input()
        if item == "End":
            break
        items.append(item)

    while items:
        if available_robots:
            current_robot = available_robots.popleft()
            if current_robot in robots.keys():
                for robot in working_robots:
                    index = 0
                    robot[1] = int(robot[1]) - 1
                    if robot[1] == 0:
                        robot[1] = str(robot[1])
                        working_robots.pop(index)
                        available_robots.append(robot[0])
                    index += 1
                index_robot_in_dict = robots[current_robot]
                working_robots.append([current_robot, index_robot_in_dict])
                time = current_time(time[0], time[1], time[2])
                print(f"{current_robot} - {items[0]} [{time[0]:02d}:{time[1]:02d}:{time[2]:02d}]")
                items.popleft()
        else:
            current_item = items.popleft()
            items.append(current_item)
            time = current_time(time[0], time[1], time[2])
            index = 0
            for robot in working_robots:
                robot[1] = int(robot[1]) - 1
                if robot[1] == 1:
                    working_robots.pop(index)
                    available_robots.append(robot[0])
                index += 1
            continue


robotics()


