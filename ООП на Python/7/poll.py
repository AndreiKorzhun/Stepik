class Initialization:
    """ Итоги опроса """
    def __init__(self, capacity, food):
        if isinstance(capacity, int):
            self.capacity = capacity
            self.food = food
        else:
            print("Количество людей должно быть целым числом")


class Vegetarian(Initialization):
    """ Результат опроса людей относящих себя к классу Vegetarian """
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        """ Возвращает количество вегетарианцев и их любимую еду """
        return f"{self.capacity} людей предпочитают не есть мясо! \
                 Они предпочитают {self.food}"


class MeatEater(Initialization):
    """ Результат опроса людей относящих себя к классу MeatEater """
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        """ Возвращает количество мясоедов и их любимую еду """
        return f"{self.capacity} мясоедов в Москве! \
                 Помимо мяса они едят еще и {self.food}"


class SweetTooth(Initialization):
    """ Результат опроса людей относящих себя к классу SweetTooth """
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        """ Возвращает количество сладкоежек и их любимую еду """
        return f"Сладкоежек в Москве {self.capacity}. \
                 Их самая любимая еда: {self.food}"

    def _compare(self, value, operator):
        """ Проверяет объект value и сравнивает его с количеством сладкоежек """
        if isinstance(value, int):
            return eval(f"{self.capacity} {operator} {value}")
        elif isinstance(value, (Vegetarian, MeatEater)):
            return eval(f"{self.capacity} {operator} {value.capacity}")
        else:
            return f"Невозможно сравнить количество сладкоежек с {value}"

    # Сравнение количества сладкоежек с числом или с количеством людей,
    # относящих себя к другому классу
    def __eq__(self, obj):
        return self._compare(obj, "==")

    def __lt__(self, obj):
        return self._compare(obj, "<")

    def __gt__(self, obj):
        return self._compare(obj, ">")
