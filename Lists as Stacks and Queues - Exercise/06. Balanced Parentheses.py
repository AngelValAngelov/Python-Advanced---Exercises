def balanced_parentheses():
    dict = {
        "{": "}",
        "[": "]",
        "(": ")"
    }
    stack_open = list()

    text = input()

    for element in text:
        if element in "{[(":
            stack_open.append(element)
        elif stack_open and element in dict.values():
            current = stack_open[-1]
            if dict[current] == element:
                stack_open.pop()
            else:
                return "NO"
        else:
            return "NO"
    if not stack_open:
        return "YES"


print(balanced_parentheses())
