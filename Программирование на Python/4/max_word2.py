# считывает файл
with open("dataset_3363_3.txt") as file:

    # создаем список считанных из файла слов приведенных к нижнему регистру
    words = file.read().lower().split()

# возвращает слово наиболее часто встречающееся в тексте
word = max(set(words), key=words.count)

print(word, words.count(word))