class Money:
    """ Подсчёт долларов и центов """

    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    def get_dollars(self):
        """ Вернуть значение в долларах """
        return self.total_cents // 100

    def set_dollars(self, dollars):
        """ Установить значение dollars и пересчитать total_cents """
        if isinstance(dollars, int) and dollars >= 0:
            self.total_cents = dollars * 100 + self.total_cents % 100
        else:
            print("Error dollars")

    def get_cents(self):
        """ Вернуть значение в центах """
        return self.total_cents % 100

    def set_cents(self, cents):
        """ Установить значение cents и пересчитать total_cents """
        if isinstance(cents, int) and 0 <= cents < 100:
            self.total_cents = (self.total_cents // 100) * 100 + cents
        else:
            print("Error cents")

    def __str__(self):
        return f"Ваше состояние составляет {self.dollars} долларов\
                {self.cents} центов"

    dollars = property(get_dollars, set_dollars)
    cents = property(get_cents, set_cents)
