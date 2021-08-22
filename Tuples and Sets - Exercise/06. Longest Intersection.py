number = int(input())

longest_intersection = list()

for i in range(number):
    numbers = input().split("-")
    first = numbers[0].split(",")
    second = numbers[1].split(",")
    first_start = first[0]
    first_end = first[1]
    second_start = second[0]
    second_end = second[1]

    intersection = set([x for x in range(int(first_start), int(first_end) + 1)]) & set([x for x in range(int(second_start), int(second_end) + 1)])
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is [{', '.join([str(x) for x in longest_intersection])}] with length {len(longest_intersection)}")