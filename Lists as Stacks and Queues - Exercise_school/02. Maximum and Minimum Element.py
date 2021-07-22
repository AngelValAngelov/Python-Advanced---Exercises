stack = []


def push(num):
    global stack
    return stack.append(num)


def delete():
    global stack
    if stack:
        return stack.pop()


def print_max_num():
    global stack
    if stack:
        print(max(stack))


def print_min_num():
    global stack
    if stack:
        print(min(stack))


number = int(input())

while number:
    command = input().split()
    if command[0] == str(1):
        n = int(command[1])
        push(n)
    if command[0] == str(2):
        delete()
    if command[0] == str(3):
        print_max_num()
    if command[0] == str(4):
        print_min_num()
    number -= 1

print(", ".join(reversed([str(x) for x in stack])))


