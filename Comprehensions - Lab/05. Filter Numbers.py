num_start = int(input())
num_end = int(input())

divisors = [x for x in range(2, 10)]

result = [x for x in range(num_start, num_end + 1) if len([True for z in range(2, 11) if x % z == 0]) > 0]

print(result)



