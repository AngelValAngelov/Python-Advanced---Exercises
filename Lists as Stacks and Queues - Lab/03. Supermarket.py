from collections import deque


def supermarket():
    people = deque(list())

    while True:
        p = input()
        if p == "Paid":
            while people:
                print(people.popleft())
        elif p == "End":
            return f"{len(people)} people remaining."
        else:
            people.append(p)


print(supermarket())
