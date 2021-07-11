def create(name_space, parent):
    ''' Создает новое пространство имен <namespace> внутри
        пространства <parent>. '''

    # Добавляет в переменную spaces <namespace> с указанием его родителя
    global spaces
    spaces[name_space] = [set(), parent]


def add(name_space, var):
    ''' Добавляет в пространство <namespace> переменную <var>. '''

    global spaces
    # <namespace> еще не создан с помощью функции create
    if name_space not in spaces:
        print('Нельзя добавить переменную ' + var +
              ' в несуществующий namespace: ' + name_space)
        return
    value = spaces[name_space]
    value[0].add(var)
    spaces[name_space] = value


def get(name_space, var):
    ''' Получить имя пространства, из которого будет взята переменная <var>
    при запросе из пространства <namespace> или None, если такого пространства
    не существует. '''

    while name_space != 'None':
        if var in spaces[name_space][0]:
            break
        else:
            name_space = spaces[name_space][1]
    print(name_space)


# Количество запросов
n = int(input())
# Набор запросов
requests = [input().split() for i in range(n)]

# Пространства имён
spaces = {'global': [set(), 'None']}

for request in requests:
    if request[0] == 'create':
        create(request[1], request[2])
    elif request[0] == 'add':
        add(request[1], request[2])
    elif request[0] == 'get':
        get(request[1], request[2])
    else:
        print('Запроса ' + request[0] + ' не существует')
