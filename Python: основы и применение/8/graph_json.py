import json

# Расшифровка JSON переданного в строке ввода
json_objects = json.loads(input())

# Преобразует объект JSON в словарь формата {имя_класса: родители}
graph = {json_obj["name"]: json_obj["parents"] for json_obj in json_objects}

# Создает словарь {имя_класса: дети} и добавляет к детям имя самого класса
out_graph = {class_name: [class_name] for class_name in graph.keys()}


def add_child(name, parents):
    ''' Для каждого родителя класса name добавляет класс в список детей '''

    # Перебирает всех родителей класса name
    for parent in parents:
        # Добавляет имя класса name в список детей класса parent
        # если оно еще не добавленно
        if name not in out_graph[parent]:
            out_graph[parent].append(name)
        # Повторяет действие для родителей родителей
        add_child(name, graph[parent])


# Для всех родителей class_parents добавь класс class_name в список детей
for class_name, class_parents in graph.items():
    add_child(class_name, class_parents)

# Вывод сортированного словаря в лексикографическом порядке на экран
for name, children in sorted(out_graph.items()):
    print(name, ":", len(children))
