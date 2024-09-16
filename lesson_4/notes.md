### Функции
Функции это блоки кода, которые можно вызывать многократно. 
Они могут принимать данные, называемые аргументами, и возвращать данные, 
называемые возвращаемыми значениями.

В объявлении функции мы должны указать имя функции и аргументы, которые она принимает.
В теле функции мы пишем код, который будет выполняться при вызове функции.
Внутри тела можно писать любой код. Это как небольшая самостоятельная программа

Пример функции которая приветсвует пользователя, печатая "Hello!" и имя пользователя.
Имя передается как аргумент функции.
```python
def greet_user(name):  # <--- Объявление функции
    print("Hello!")  # <--- Тело функции
    print(name)  # <--- Тело функции, name это аргумент функции

greet_user("Dasha")  # <--- Вызов функции
```

Дальше лучше попробовать в уме построчно выполнить
код и потом запустить его и проверить что все верно.

```python
def greet_user(name):
    print("Hello!")
    print(name)

greet_user("Dasha")
greet_user("Oleg")
```

```python
print(1)
def greet_user(name):
    print("Hello!")
    print(name)

print(2)
greet_user("Sirgay")
print(3)
greet_user("John")
```

```python
print(1)
def greet_user(name):
    print("Hello!")
    print(name)
    print(2)
print(3)

greet_user("John")
```

У функции не обязательно должны быть аргументы.
```python
def greet_oleg():
    print("Hello Oleg!")

greet_oleg()
greet_oleg()
```

У фукнции может быть выходное значение.
```python
def greet_user_and_return_name(name):
    print("Hello!")
    print(name)
    return name  # <--- Возвращаемое значение

name = greet_user_and_return_name("Dasha")
print(name)
```

Функция всегда заканчивается когда встречает return.
```python
def example():
    print(1)
    return
    print(2)  # <--- Этот код никогда не выполнится тк находится ниже return, но при этом код не вызовет ошибку

example()
```

Аргументов может быть много.
```python
def print_user_info(name, age, gender, city, country, job):
    print(name)
    print(age)
    print(gender)
    print(city)
    print(country)
    print(job)

print_user_info("Oleg", 27, "Male", "Perm", "Russia", "Unemployed")
```

Код ниже неправильный
```python
def print_user_info(name, age, gender, city, country, job):
    print(name)
    print(age)
print(gender)  # если ты сместила эту строку влево, то пайтон начинает считать что тело закончилось, но дальше он опять видит тело и не понимает что происходит
    print(city)
    print(country)
    print(job)

print_user_info("Oleg", 27, "Male", "Perm", "Russia", "Unemployed")
```

Теперь для самостоятельного написания:
- Напиши функцию которая принимает два числа и возвращает их сумму.
- Напиши функцию которая принимает два числа и возвращает их произведение.
- Напиши функцию которая принимает имя пользователя ничего с ним не делает и возврает его из функции (return)def
