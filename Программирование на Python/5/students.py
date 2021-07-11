# открывает файл
with open("dataset_3363_4.txt") as file:
    
    students = []

    # записывает в список студентов и их оценки по предметам
    for line in file:
        students.append(line.split(";"))

    width = len(students[0])
    # количество студентов
    num_students = len(students)
    # сумма оценок по предметам
    sum_1, sum_2, sum_3  = 0, 0, 0

    for student in students:
        # средняя оцентка студента по всем предметам
        avr = sum([int(j) for j in student[1:]]) / (width - 1)
        # округление до 9 знаков после запятой
        print(round(avr, 9))

        sum_1 += int(student[1])
        sum_2 += int(student[2])
        sum_3 += int(student[3])

print(sum_1 / num_students, sum_2 / num_students, sum_3 / num_students)