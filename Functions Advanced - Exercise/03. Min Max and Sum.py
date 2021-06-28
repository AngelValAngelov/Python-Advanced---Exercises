def min_max_xum(nums):
    print(f"The minimum number is {min(int(x) for x in nums)}")
    print(f"The maximum number is {max(int(x) for x in nums)}")
    print(f"The sum number is: {sum([int(x) for x in nums])}")


numbers = input().split()

min_max_xum(numbers)
