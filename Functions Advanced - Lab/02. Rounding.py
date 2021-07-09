def abs_numbers(values):
    return [round(x) for x in values]


print(abs_numbers(map(float, input().split())))
