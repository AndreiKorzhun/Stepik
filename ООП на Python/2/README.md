## 2.6 Геттеры и сеттеры, property атрибуты


Создайте класс UserMail, у которого есть:

- конструктор **\_\_init__**, принимающий 2 аргумента: логин и почтовый адрес. Их необходимо сохранить в экземпляр как атрибуты **login** и **\_\_email** (обратите внимание, защищенный атрибут)
- метод геттер **get_email**, которое возвращает защищенный атрибут **\_\_email** ;
- метод сеттер **set_email**, которое принимает в виде строки новую почту. Метод должен проверять, что в новой почте есть только один символ @ и после нее есть точка. Если данные условия выполняются, новая почта сохраняется в атрибут **\_\_email**, в противном случае выведите сообщение "Ошибочная почта";
- создайте свойство **email**, у которого геттером будет метод **get_email**, а сеттером - метод **set_email**.

``` python
k = UserMail('belosnezhka', 'prince@wait.you')
print(k.email)  # prince@wait.you
k.email = [1, 2, 3] # Ошибочная почта
k.email = 'prince@still@.wait'  # Ошибочная почта
k.email = 'prince@still.wait'
print(k.email)  # prince@still.wait
```
