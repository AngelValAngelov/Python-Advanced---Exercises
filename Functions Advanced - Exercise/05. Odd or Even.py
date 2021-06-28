def odd_sum(nums):
    return sum(filter(lambda x: x % 2 == 1, nums)) * len(nums)


def even_sum(nums):
    return sum(filter(lambda x: x % 2 == 0, nums)) * len(nums)


def odd_or_even(even_or_odd, n):
    if even_or_odd == 'Odd':
        return odd_sum(n)
    else:
        return even_sum(n)


odd_even = input()
numbers = list(map(int, input().split()))

print(odd_or_even(odd_even, numbers))