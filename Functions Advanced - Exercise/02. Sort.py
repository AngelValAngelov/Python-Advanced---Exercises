def sort(nums):
    result = sorted([int(x) for x in nums])
    return result


numbers = input().split()

print(sort(numbers))