import requests
import json
import operator


# client_id и client_secret выдаются при регистрации
# на сайте https://developers.artsy.net/start
client_id = '...'
client_secret = '...'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)
# достаем токен
token = j["token"]


def get_json(url):
    # создаем заголовок, содержащий токен
    headers = {"X-Xapp-Token": token}
    # инициируем запрос с заголовком
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    # возвращает ответ сервера
    return json.loads(res.text)


# создаем словарь для хранения имен художников и дат их рождения
names = dict()

with open("dataset_24476_4.txt", "r") as artists:
    for artist in artists:
        # инициируем запрос с заголовком
        r = get_json(
            "https://api.artsy.net/api/artists/{}".format(artist.rstrip()))

        # помещаем в словарь имя и дату рождения художника
        names[r['sortable_name']] = r['birthday']

# сортировка словаря по значению(по возрастанию) и по ключу
# (в лексикографическом порядке), получаем лист кортежей [(), ()]
names = sorted(names.items(), key=operator.itemgetter(1, 0))

# вывод имен
for name in names:
    print(name[0])
