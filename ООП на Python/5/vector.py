class Vector:
    """ Хранит в себе вектор целых чисел """

    def __init__(self, *args):
        self.values = sorted([arg for arg in args if isinstance(arg, int)])

    def __str__(self):
        """ Вывод значений вектора """
        if self.values:
            return f"Вектор{*self.values,}"
        return "Пустой вектор"

    def __len__(self):
        return len(self.values)

    def __add__(self, obj):
        """ Сложение значений вектора с числом или другим вектором """
        if isinstance(obj, int):
            return Vector(*[value + obj for value in self.values])
        elif isinstance(obj, Vector):
            if len(self) == len(obj):
                return Vector(*[self.values[i] + obj.values[i]
                                for i in range(len(self))])
            return print("Сложение векторов разной длины недопустимо")
        return print(f"Вектор нельзя сложить с {obj}")

    def __mul__(self, obj):
        """ Умножение значений вектора с числом или другим вектором """
        if isinstance(obj, int):
            return Vector(*[value * obj for value in self.values])
        elif isinstance(obj, Vector):
            if len(self) == len(obj):
                return Vector(*[self.values[i] * obj.values[i]
                                for i in range(len(self))])
            return print("Умножение векторов разной длины недопустимо")
        return print(f"Вектор нельзя умножать с {obj}")
