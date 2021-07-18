def max_and_min_element(num):
    stack = list()
    for i in range(num):
        query = input().split()
        command = int(query[0])
        if command == 1:
            n = int(query[1])
            stack.append(n)
        elif command == 2:
            if len(stack) >= 1:
                stack.pop()
        elif command == 3:
            if stack:
                print(max(stack))
        elif command == 4:
            if stack:
                print(min(stack))

    print(", ".join(str(x) for x in reversed(stack)))


number = int(input())
max_and_min_element(number)
