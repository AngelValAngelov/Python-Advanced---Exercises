words = input().split()

result = [x for x in words if len(x) % 2 == 0]

[print(x) for x in result]