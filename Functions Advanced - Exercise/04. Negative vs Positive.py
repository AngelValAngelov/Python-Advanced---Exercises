def summ(positive, negative):
    if sum(positive) > sum([abs(x) for x in negative]):
        print(sum(negative))
        print(sum(positive))
        print("The positives are stronger than the negatives")
    else:
        print(sum(negative))
        print(sum(positive))
        print("The negatives are stronger than the positives")


def negative_positive(nums):
    positive_numbers = list()
    negative_numbers = list()
    for x in nums:
        if int(x) < 0:
            negative_numbers.append(int(x))
        else:
            positive_numbers.append(int(x))
    summ(positive_numbers, negative_numbers)


numbers = input().split()

negative_positive(numbers)
