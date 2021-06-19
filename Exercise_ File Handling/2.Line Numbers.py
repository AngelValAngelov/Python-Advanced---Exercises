file_path = '../Exercise_ File Handling/text.txt'

with open(file_path, "r") as file:
    index = 0
    final = ""
    for row in file:
        index += 1
        length = 0
        counter = 0

        for symbol in row:
            if symbol.isalpha():
                length += 1
            if symbol in "',.!?\":-_":
                counter += 1
        final += f"Line {index}: {row[:-2]} ({length})({counter})\n"

with open('output.txt', 'w') as file:
    file.write(final)