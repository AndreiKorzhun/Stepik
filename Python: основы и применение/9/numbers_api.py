import requests


# Открывает файл с числами
with open("dataset.txt") as numbers:

    for number in numbers:
        # Убирает символ перевода строки после числа
        number = number.rstrip()
        url = "http://numbersapi.com/{}/math?json=true"
        # Запрос get
        res = requests.get(url.format(number))
        # Преобразует json-формат представления данных в словарь python
        # аналог: data = json.loads(res.text)
        data = res.json()

        if data['found']:
            print(data['text'])
        else:
            print("{} is boring.".format(number))
