def sum_numbers(num_1, num_2):
    return num_1 + num_2


def multiply_numbers(nun_1, num_2):
    return nun_1 * num_2


def func_executor(*args):
    result = list()
    for x in args:
        func = x[0]
        nums = x[1]
        result.append(func(*nums))
    return result

print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
