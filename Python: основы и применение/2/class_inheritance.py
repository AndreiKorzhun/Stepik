# Создает словарь <имя класса>:[родители]
graph = dict()
for _i in range(int(input())):
    lst = input().split()
    graph[lst[0]] = lst[2:]


def recurse(class_name, parents):
    ''' Ищет <имя класса 1> в родителях <имя класса 2>. '''
    global ans
    if class_name in parents:
        ans = True
    else:
        for parent in parents:
            recurse(class_name, graph[parent])


# Запросы в формате <имя класса 1> <имя класса 2>
for _i in range(int(input())):
    class_name1, class_name2 = input().split()

    # <имя класса 1> или <имя класса 2> не объевлены в словаре graph
    if class_name1 not in graph.keys() or class_name2 not in graph.keys():
        print("No")
    else:
        ans = False
        # Ищет <имя класса 1> в родителях <имя класса 2>
        recurse(class_name1, graph[class_name2])
        # <имя класса 1> является предком самого себя или найден
        # в родителях <имя класса 2>
        if class_name1 == class_name2 or ans is True:
            print("Yes")
        else:
            print("No")
