import csv
import time
import collections

# Список совершенных типов преступлений в 2015г
type = []

# Открывает файл csv
with open("Crimes.csv") as file:
    # Создает словарь для каждой строки, считанной из файла
    crimes = csv.DictReader(file)

    for crime in crimes:
        # Находит все преступления совершенные в 2015г
        # crime["Date"] = "12/24/2021 08:45:12 AM"
        if time.strptime(
                crime["Date"],
                "%m/%d/%Y %I:%M:%S %p").tm_year == 2015:
            # Добавляет тип преступления в ранее созданный список
            type.append(crime["Primary Type"])

# Возвращает список из "n" наиболее распространенных типов преступлений и
# их количество
print(collections.Counter(type).most_common(1))
