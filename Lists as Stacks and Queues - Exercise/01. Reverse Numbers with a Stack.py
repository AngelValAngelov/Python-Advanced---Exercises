text = input().split()


def reverse_numbers(str):
    rev_text = list()
    for i in reversed(text):
        rev_text.append(i)

    return " ".join(rev_text)


print(reverse_numbers(text))
