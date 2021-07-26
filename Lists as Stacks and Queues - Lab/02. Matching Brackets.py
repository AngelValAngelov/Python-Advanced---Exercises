def matching_brackets(expression):
    index_open_brackets = list()

    for element in range(len(expression)):
        if expression[element] == "(":
            index_open_brackets.append(element)
        if expression[element] == ")":
            last_open_bracket = element + 1
            ch = index_open_brackets.pop()
            print(expression[ch:last_open_bracket])


matching_brackets(input())
