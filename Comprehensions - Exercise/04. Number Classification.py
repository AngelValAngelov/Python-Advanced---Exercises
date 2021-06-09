numbers = [int(x) for x in input().split(", ")]

positive = list()
negative = list()
even = list()
odd= list()

[positive.append(str(x)) for x in numbers if x >= 0]
[negative.append(str(x))for x in numbers if x < 0]
[even.append(str(x)) for x in numbers if x % 2 == 0]
[odd.append(str(x)) for x in numbers if x % 2 == 1]

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")