import os
import os.path


# Список директорий, в которых есть хотя бы один файл с расширением ".py".
lst_dirs = []

with open("file.txt", "w") as file_out:

    # Для каждого каталога возвращает кортеж (путь к каталогу, список
    # каталогов, список файлов)
    for current_dir, _dirs, files in os.walk("main/", "r"):
        # Перебирает файлы и ищет файлы с расширением .py
        for file in files:
            if file.endswith(".py"):
                # Вычисляет путь относительно директории start и добавляет его
                # в список директорий
                lst_dirs.append(os.path.relpath(current_dir, start="."))
                break

    # Запись в файл путей отсортированных в лексикографическом порядке
    lst_dirs.sort()
    file_out.writelines("\n".join(lst_dirs))
