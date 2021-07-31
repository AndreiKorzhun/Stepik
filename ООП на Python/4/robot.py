class Robot:
    population = 0

    def __init__(self, name):
        """ Инициализация робота """
        self.name = name
        print(f"Робот {self.name} был создан")
        Robot.population += 1
        self.__is_existing = True

    def destroy(self):
        """ Уничтожает робота """
        if self.__is_existing:
            Robot.population -= 1
        self.__is_existing = False
        print(f"Робот {self.name} был уничтожен")

    def say_hello(self):
        """ Приветствие робота """
        print(f"Робот {self.name} приветствует тебя, особь человеческого рода")

    @staticmethod
    def how_many():
        """ Выводит оставшееся количество роботов """
        print(f"{Robot.population}, вот сколько нас еще осталось")
