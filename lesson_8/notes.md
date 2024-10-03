### Условные конструкции
На сленге иф условия или просто иф/ифы

Полный синтаксис
```python
age = 10
if age <= 10:  # Иф всегда начинается с ключего слова if
    print("child")
elif age <= 30:  # elif - else if. Если первое условие не выполнилось, то проверяется второе
    print("young")
elif age <= 60: # Если второе условие не выполнилось, то проверяется третье, elif может быть сколько угодно
    print("adult")
else: # Если ни одно из условий не выполнилось, то выполняется блок else
    print("old")
```

Обязательным блоком является только первый if, все остальные блоки не обязательны
``` python
if age <= 10:
    print("child")
```

Внутри тела ифа может быть любой код
```python
age = 1
if age <= 10:
    print("child")
    print("child")
    print("child")
    print("child")
    print("child")
    a = 5
    print(a)
# Выведет 5 раз слово child и число 5
```

Внутри ифа могут быть другие ифы
```python
age = 10
if age <= 5:
    print("child")
    if age == 5:
        print("5 years old")
    elif age == 4:
        print("4 years old")
    elif age == 3:
        print("3 years old")
    elif age == 2:
        print("2 years old")
    elif age == 1:
        print("1 years old")
    elif age == 0:
        print("0 years old")
    else:
        print("Not a human")  # Отрицательный возраст, явно не ребенок
else:
    print("Not a child")
```

Часто в коде есть несколько ифоф подряд с точки зрения языка это разные иф условия идущие подряд
```python
if True:
    print("1")
if True:
    print("2")
if False:
    print("3")
else:
    print("special")
if True:
    print("4")
# Выведет 1, 2, special, 4
```

Часто в однои ифе проверяется несколько условий сразу с помощь or или and
```python
age = 10
sex = "Man"
if age <= 10 and sex == "Man":
    print("Man child")
elif age <= 10 and sex == "Woman"
    print("Woman child")
else:
    print("Not a child")
```

Некоторые типы данных могут быть приведены к булевому типу, например
```python
if 1:  # True
    print("1")
if 2:  # True
    print("2")
if 0:  # False
    print("0")
if "":  # False, это строка в которой ничего нет
    print("empty string")
if "any not empty string":  # True
    print("any not empty string")
if None:  # False
    print("None")
```
Попробуй запустить код выше

В кратце все что "похоже" на фолс в иф условие будет фолсом
Например 0, "", None

Здесь нужен опыт чтобы понять фолс это или нет не запуская код

### Домашнее задание
##### Задание 1
Напоминаю программу которую мы написали вместе с тобой
```python
real_password = "1234"
def login(password):
    if password == real_password:
        return True
    else:
        return False

login("1234")  # True
login("12345")  # False
```

Усложняем нашу функцию login, теперь у нас есть не только пароль но и имя пользователя
```python
real_password = "1234"
real_username = "oleg"
```
Теперь фунция login должна принимать 2 аргумента username и password
и проверять что оба аргумента равны real_username и real_password и только тогда возвращать True

##### Задание 2
Напоминаю программу которую мы написали вместе с тобой
```python
real_password = "1234"
def login(password):
    if password == real_password:
        return True
    else:
        return False

login("1234")  # True
login("12345")  # False
```
На самом деле ее можно упростить до
```python
real_password = "1234"
def login(password):
    return password == real_password

login("1234")  # True
login("12345")  # False
```
Задание на подумать почему это работает

##### Задание 3
Хочу показать тебе пример функции логин из реального кода, задание заключается просто в том чтобы посмотреть как примерно
выглядит реальный код чтобы ты не так сильно его боялась :)
https://github.com/django/django/blob/1feedc8ef8a34484cb5afe33f5c45b543b860210/django/contrib/auth/backends.py#L36

Если пройдешь по ссылке то увидишь функцию authenticate, она по сути делает то же самое что наша функция login

На самом деле именно на этой функции работает login половины интернета который написан с помощью python

Она чуть сложнее и там есть незнакомый тебе синтаксис, но в целом это тоже просто иф условие, проверка самого пароля находится
вот в этой строчке
https://github.com/django/django/blob/1feedc8ef8a34484cb5afe33f5c45b543b860210/django/contrib/auth/backends.py#L48

##### Задание 4
Кидаю ссылку на обещанный курс по пайтон, можешь его потихньку начинать
https://ru.hexlet.io/courses/python-basics/lessons/intro/theory_unit
