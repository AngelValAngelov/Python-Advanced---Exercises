from collections import deque


def biggest_client():
    global all_cl
    best_client = max([x for x in all_cl])
    return best_client


all_food = int(input())
clients = deque(input().split())

all_cl = [int(x) for x in clients]

while clients:
    if all_food - int(clients[0]) >= 0:
        c = clients.popleft()
        all_food -= int(c)
    else:
        break

if clients:
    print(biggest_client())
    print(f"Orders left: {' '.join(str(x) for x in clients)}")
else:
    print(biggest_client())
    print("Orders complete")