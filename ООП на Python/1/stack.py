class Stack:
    """ Реализация  стека(stack) """
    def __init__(self):
        self.values = []

    def push(self, item):
        """ Добавляет новый элемент на вершину стека """
        self.values.append(item)

    def pop(self):
        """ Удаляет верхний элемент из стека """
        if self.is_empty():
            print("Empty Stack")
            return None
        else:
            return self.values.pop()

    def peek(self):
        """ Возвращает верхний элемент стека, но не удаляет его """
        if self.is_empty():
            print("Empty Stack")
            return None
        else:
            return self.values[-1]

    def is_empty(self):
        """ Проверяет стек на пустоту """
        return self.size() == 0

    def size(self):
        """ Возвращает количество элементов в стеке """
        return len(self.values)
