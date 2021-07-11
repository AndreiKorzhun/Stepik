# открывает два файла, один для чтения, второй для записи
with open("dataset_3363_2.txt", "r") as file_in, \
        open("file.txt", "w") as file_out:

    line = file_in.read()

    length = len(line)
    # позиция симфола(буквы)
    i = 0

    while i < length - 1:
        # позиция символа(цифры)
        x = i + 1
        # число стоящее за буквой
        num = 0

        # перебирает символы, пока не определит число стоящее после буквы
        while line[x].isdigit():
            num = num * 10 + int(line[x])
            x += 1

        # печатает в файл строку необходимиго формата
        for _ in range(num):
            file_out.write(line[i])

        # переход к следующей букве
        i = x
