def even_numbers(nums):
    return list(filter(lambda x: x % 2 == 0, nums))


numbers = map(int, input().split())

print(even_numbers(numbers))
