def reversed_string(text):
    s = list()
    for letter in text:
        s.append(letter)

    new_s = list()
    while s:
        char = s.pop()
        new_s.append(char)

    return "".join(new_s)


print(reversed_string(input()))