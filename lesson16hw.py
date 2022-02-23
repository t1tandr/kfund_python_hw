# ex 1
# def send_message(name):
#     print(f'Hi, {name.title()}')

# x = input('Введите ваше имя: ')
# send_message(x)

# ex 2

# def send_message(text, count):
#     print(f'{text}\n' *count)
# text = input('Введите текст: ')
# count = int(input('Введите количество строк: '))
# send_message(text, count)

# ex 3

# def send_message(text, count):
#     print(f'{text}\n' *count)
# text = input('Введите текст: ')
# count = int(input('Введите количество строк: '))
# send_message(text, count)

# ex 4

# def send_message(text, count):
#     print(f'{text}\n' *count)
# text = input('Введите текст: ')
# count = int(input('Введите количество строк: '))
# send_message(text, count)

# ex 5

# def send_message(text, count):
#     print(f'{text}\n' *count)
# text = input('Введите текст: ')
# count = int(input('Введите количество строк: '))
# send_message(text, count)

# ex 6

# def max_number(i, g):
#     if i == g:
#         print('equal')
#     elif i > g:
#         print(f'{i} is greater')
#     else:
#         print(f'{g} is greater')
# i = int(input('Введите первое число: '))
# g = int(input('Введите второе число: '))
# max_number(i, g)

# ex 7

# first = int(input('Введите 1 число: '))
# second = int(input('Введите 2 число: '))
# third = int(input('Введите 3 число: '))
# def max_number(x, y, z):
#     list = []
#     list.append(x)
#     list.append(y)
#     list.append(z)
#     print(f'Максимальное число: {max(list)}')

# max_number(first,second,third)

# ex 8

# def trykut(a, b, c):
    # if a + b > c and a + c > b and b + c > a:
    #     print('its true')
    # else:
    #     print('false')
# a = int(input('Введите значение 1 стороны: '))
# b = int(input('Введите значение 2 стороны: '))
# c = int(input('Введите значение 3 стороны: '))
# trykut(a, b, c)

# ex 9

# def plus(a,b):
#     x = a
#     x += f' {b}'
#     print(x)
# a = input('Введите первое слово: ')
# b = input('Введите второе слово: ')
# plus(a,b)

# ex 10

# def operation(x, y, z):
#     if z == '+':
#         answer = x + y
#     elif z == '-':
#         answer = x - y
#     elif z == '*':
#         answer = x * y
#     elif z == '/':
#         answer = x / y
#     else:
#         print('Unknown')
#     return answer


# a = int(input('Введите 1 число: '))
# b = int(input('Введите 2 число: '))
# x = input('Введите операцию: ')
# print(round(operation(a,b,x), 2))

# ex 11

# def dohtml(a, b):
#     print(f'<{b}> {a} </{b}>')
# teg = input('Введите тег ХТМЛ: ')
# text = input('Введите текст внутри тега: ')
# dohtml(text, teg)

# ex 12

# def season(a):
#     if a == 1 or a == 2 or a == 12:
#         print(f'{a} месяц принадлежит зиме')
#     if a >= 3 and a <= 5:
#         print(f'{a} месяц принадлежит весне')
#     if a >= 6 and a <= 8:
#         print(f'{a} месяц принадлежит лету')
#     if a >= 9 and a <= 11:
#         print(f'{a} месяц принадлежит осени')
#     else:
#         print('Такого месяца нет')
# month = int(input('Введите номер месяца: '))
# season(month)

# ex 13

# def message(text, list):
#     # dlina = len(list)
#     for i in list:
#         print(f'{text * i}*')
# text = input('Введите символ. который будет отображаться n раз: ')
# list = []
# print("для выхода введите 'stop' ")
# while True:
#     a = input('Введите число символов на рядке: ')
#     if a == 'stop':
#         break
#     else:
#         list.append(int(a))

# message(text, list)

# ex 14

# def parn(a):
#     if a%2 == 0:
#         print(f'Число {a} - парное')
#     else:
#         print(f'Число {a} - непарное')

# a = int(input('Введите число: '))
# parn(a)

# ex 15

# def max_and_min(list):
#     list2 = []
#     list2.append(list[0])
#     list2.append(list[-1])
#     print(list2)

# print("Чтобы остановить последовательность - введите 'stop'")
# list = []
# while True:
#     a = input('Введите число: ')
#     if a == 'stop':
#         break
#     else:
#         list.append(int(a))

# max_and_min(list)

# ex 16

# def factorial(a):
#     ans = 1
#     while a > 0:
#         ans *= a
#         a -= 1
#     print(ans)
# a = int(input('Введите число: '))
# factorial(a)

# ex 17
import math

def s(obj, a, b, c):
    if obj == 'треугольник':
        if a + b > c and a + c > b and b + c > a:
            p = (a+b+c)/2
            ploscha = math.sqrt((p*(p-a)*(p-b)*(p-c)))
            print(f'Площадь фигуры = {int(ploscha)}')
        else:
            print('Такого треугольника не бывает')

    if obj == 'прямоугольник':
        print(f'Площадь фигуры = {(a*2) + (b*2)}')
    if obj == 'круг':
        print(f'Площадь фигуры = {a**2*3.14}')
object = input('Введите название фигуры (треугольник, прямоугольник, круг): ')
a = int(input('Введите 1 значение: '))
b = int(input('Введите 2 значение(если не нужно - введите 0): '))
c = int(input('Введите 3 значение(если не нужно - введите 0): '))

s(object, a, b, c)
