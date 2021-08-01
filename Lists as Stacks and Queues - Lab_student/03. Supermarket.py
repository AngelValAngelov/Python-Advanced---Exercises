from collections import deque

deque = deque()
counter = 0

while True:
    word = input()
    if word == "Paid":
        while deque:
            print(deque.popleft())
            counter -= 1
    if word == "End":
        print(f"{counter} people remaining.")
        break
    if word != "Paid" and word != "End":
        deque.append(word)
        counter += 1