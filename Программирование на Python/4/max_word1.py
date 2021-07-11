# считывает файл
with open("dataset_3363_3.txt") as file:

    word = ""
    max = 0

    # создаем сортированный список считанных из файла слов 
    # приведенных к нижнему регистру
    words = sorted(file.read().lower().split())


i, j = 0, 0

# подсчитывет количество повторений слова в списке
while i < len(words):
    count = 0

    while j < len(words):
        if words[i] == words[j]:
            count += 1
            j += 1
        else:
            break
    
    if count > max:
        max = count
        word = words[i]
        
    i += count

print(word, max)