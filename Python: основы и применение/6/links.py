import re
import requests


# ссылка на HTML файл
link = input()
# находит в HTML файле все ссылки вида <a ... href="..." ... >
urls = re.findall(r'''<a.+href=[\"\']\w*:\/\/(\w+[\w\.-]*)''',
                  requests.get(link).text)

# убирает дубликаты ссылок
urls = set(urls)

# вывод ссылок в алфавитном порядке
for url in sorted(urls):
    print(url)
