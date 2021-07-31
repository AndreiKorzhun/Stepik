import re


class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        """ Возвращает значение email """
        return self.__email

    def set_email(self, email):
        """ Проверяет и изменяет значение email """
        if isinstance(email, str) and re.match(r'\w+@[^@]\w*\.\w*$', email):
            self.__email = email
        else:
            print("Ошибочная почта")

    email = property(get_email, set_email)
