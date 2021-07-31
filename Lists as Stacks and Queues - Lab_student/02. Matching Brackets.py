numbers = input()

stack_open_brackets = []

for i in range(len(numbers)):
    if numbers[i] == "(":
        index = numbers[i]
        stack_open_brackets.append(i)
    if numbers[i] == ")":
        index = i
        start_index = stack_open_brackets.pop()
        print(numbers[start_index: index + 1])











