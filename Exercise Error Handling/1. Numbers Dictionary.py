numbers = {}

line = input()

try:
    while line != "Search":
        number_str = line
        number = int(input())
        numbers[number_str] = number
        line = input()

    line = input()

    while line != "Remove":
        searched = line
        print(numbers[searched])
        line = input()

    line = input()

    while line != "End":
        searched = line
        del numbers[searched]
        line = input()

except ValueError:
    print("The variable number must be an integer")

except KeyError:
    print("Number does not exist in dictionary")

print(numbers)