def calculate(list_nums):
    d = {}
    for value in list_nums:
        if value not in d:
            d[value] = 1
        else:
            d[value] += 1

    for key, value in d.items():
        print(f"{key} - {value} times")


list_nums = input().split()
list_nums = [float(x) for x in list_nums]

calculate(list_nums)