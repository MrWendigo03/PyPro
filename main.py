#iterator
from io import TextIOBase
from typing import Iterable, Callable

import requests

# Первый урок
# Мой коммент
# Типы данных
# Числовые:
# int - целые
# float - Дробные
# complex - Комплексные
# Исчисляемые:
# str - Строка
# list - Список
# tuple - Кортеж
# dict - Словарь
# set - Множества

"""int_1 = 1
float_1 = 1.2
complex_1 = 1j
str_1 = "hello2"
str_2 = '2'
list_1 = [1, 2, 3, "4"]
tuple_1 = (1, 2, 3, "4")
dict_1 = {1: 20}
set_1 = {1, 2, 3, 4, 4}"""
# print(set_1)

'''print(1)
print("2")
print(True)
text = "Hello World!"
print(text)
text = 1
print(text)
text = True
print(text)'''

'''print (12 + 1)
print (12 - 13)
print (12 / 5)
print (12 // 5)
print (12 % 11)
print (16 ** 2)
print (3 * 7)
print (1 + '1')
print (1 - '1')
print ('1' * 10)
print ("10" * 2)
print ('1' + "1")
print ("1" - '1')'''

# print ('\nHello world\ngoodbye world\n\n    hello again\n')

'''name = "Azizbek"
age = 19
age = str(age)
print(name, age)
print(name + " " + age)
print(f"my name is {name}, I'm {age}")
print("my name is {0}, I'm {1}".format(name, age))
# print(age)
print("hello %s i am %s" %(name, age))'''

'''print("Введи число")
name = int(input("ДА ВВЕДИ УЖЕ ЧИСЛО\n"))
print(name + 200)'''

# Второй урок
'''Сравнение
>, <, >=, <=, ==, !=
print (10 > 20)
print (10 >= 20)
print (10 < 20)
print (10 <= 20)
print (10 == 20)
print (10 != 20)'''

'''print ("Aziz" > "Azazel")
print ("Aziz" >= "Azazel")
print ("Aziz" < "Azazel")
print ("Aziz" <= "Azazel")
print ("Aziz" != "Azazel")
print ("Aziz" == "Azazel")'''

# ord принемает 1 символ

"""a = "Aziz".lower
print(a)
a = "Aziz".upper
print(a)
a = "Aziz-azizbek=aza az".title
print(a)
a = "aziz".capitalize
print(a)"""

# Списки
"""list1 = []
list2 = list()
print(list1)
print(list2)"""

class matrix_output:

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.counter == start

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.end:
            raise StopIteration
        value = self.counter
        self.counter += 1
        return value

    def my_for(iterable: Iterable, body_func: Callable):
        iter_object = iterable.__iter__()
        while True:
            try:
                value = next(iter_object)
            except StopIteration:
                break
            else:
                body_func(value)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]


matrix_output(matrix, print())
