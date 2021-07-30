def str(s):
    list = []
    for i in s:
        list.append(i)

    return list


string = input()


def solve():
    reversed_list = []
    l = str(string)
    while l:
        reversed_list.append(l.pop())

    return "".join(reversed_list)


print(solve())
