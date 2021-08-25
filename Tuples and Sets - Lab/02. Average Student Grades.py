num = int(input())


def grades_names():
    for names, grades in names_grades.items():
        name = names
        grade = [float(x) for x in grades]
        g = ' '.join([f"{x:.2f}" for x in grade])
        average_grade = sum(grade) / len(grades)
        print(f"{name} -> {g} (avg: {round(average_grade , 2):.2f})")


names_grades = {}

while num:
    name_grade = input().split(" ")
    name = name_grade[0]
    grades = name_grade[1]

    if name not in names_grades:
        names_grades[name] = [grades]
    else:
        names_grades[name].append(grades)

    num -= 1

grades_names()
