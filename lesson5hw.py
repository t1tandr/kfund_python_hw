import math
p = math.pi
e = math.e

#zadacha1
# r = int(input('Введите радиус: '))
# s = p*(r**2)
# print(f'Площадь круга с радиусом {r} равна {s} единиц квадратных')

#zadacha 2

# parol = "akjshdg23"
# int_parol = str(input('Введите пароль'))

# if int_parol == parol:
#     print('Вы ввели правильный пароль')
# else:
#     print('Вы ввели неверный пароль')

#3 zadacha
# name = input('Введите ваше имя: ')
# age = 20
# review = 'good'
# history = 'good'
# if age > 18 and review != 'bad' and history == 'good':
#     print(f'Поздравляем, {name}, вы можете взять кредит!')
# else:
#     print('{name}, k сожалению у вас нету права на кредит')

# 4 zadacha(ya poschital chto tut udobneye budet sdelat` zadaniye s pomoschyu spiskov`)

# marks = []

# while True:

#     mark_input = input("Введите текущую оценку: (если текущие оценки закончились, то введите 'stop': )")

#     if mark_input != 'stop':
#         mark_input_int = int(mark_input)
#         marks.append(mark_input_int)
#     else:
#         # print(marks)
#         break

# dlina = len(marks)
# # print(dlina)
# sum = 0
# for i in marks:
#     sum += i

# avg = sum/dlina
# print(f'Средний бал ученика составляет {avg} бала')

# 5 zadacha

# x = int(input('ВВедите X: '))
# y = int(input('ВВедите Y: '))

# if x > y:
#     z = math.sqrt(x*y)
#     print(z)
# else:
#     z = math.log(x+y, e)
#     print(z)

# 6 zadacha

# temp = float(input('Введите температуру: '))
# if temp > 20:
#     print('on')
#     print(f'Кондиционер включен, так как температура воздуха в комнате составляет: {temp} градусов')
# else:
#     print('off')
#     print(f'Кондиционер выключен, так как температура воздуха в комнате составляет {temp} градусов')

# 7 zadacha

# n = int(input('Введите номер под которым стоит молодой человек: '))
# if n % 2 == 0:
#     print('Молодой человек скажет что он под номером два')
# else:
#     print('Молодой человек скажет, что он стоит под номером 1')

# 8 zadacha

# a = int(input('Введите первую сторону: '))
# b = int(input('Введите вторую сторону: '))
# c = int(input('Введите третью сторону: '))
# if a + b > c and a + c > b and b + c > a:
#     print('Существование такого треугольника возможно')
# else:
#     print('Существование такого треугольника невозможно')


# 9 zadacha

# x = int(input('Введите координату Х: '))
# y = int(input('Введите координату У: '))

# if x > 0 and y > 0:
#     print('Точка принадлежит первой координатной четверти')
# elif x < 0 and y > 0:
#     print('Точка находится во второй координатной четверти')
# elif x < 0 and y < 0:
#     print('Точка принадлежит третьей координатной четверти')
# else:
#     print('Точка находится в четвертой координатной четверти')

# 10 zadacha

# x = int(input('Введите значение X: '))
# if x > 0:
#     y = 2 * x - 10
#     print(y)
# elif x == 0:
#     y = 0
#     print(y)
# else:
#     y = 2 * abs(x) - 1
#     print(y)
