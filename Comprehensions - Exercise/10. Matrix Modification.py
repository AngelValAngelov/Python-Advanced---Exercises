number_of_matrix = int(input())

matrix = [[int(x) for x in input().split()] for y in range(number_of_matrix)]

while True:
    action = input().split()
    if action[0] == "END":
        break
    act = action[0]
    row = int(action[1])
    col = int(action[2])
    number = int(action[3])
    if 0 <= row < number_of_matrix and 0 <= col < number_of_matrix:
        if act == "Add":
            matrix[row][col] += number
        elif act == "Subtract":
            matrix[row][col] -= number
    else:
        print("Invalid coordinates")


[print(' '.join([str(y) for y in x])) for x in matrix]