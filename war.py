import random
# расходы на автомобиль
# def main():
#     toplivo = int(input('Введите расходы на топливо'))
#     remont = int(input('Введите расходы на ремонт'))
#     strahovka = int(input('Введите расходы на страховку'))
#     to = int(input('Введите расходы на ТО'))
#     sum = toplivo + remont + strahovka + to
#     print(f'Средний расход в месяц на автомобиль составляет {sum} гривен')
#     print(f'Средний расход в год на автомобиль составляет {sum*12} гривен')
#
# main()

# def stadium():
#     a = int(input('Введите количество билетов проданное на сектор А: '))
#     b = int(input('Введите количество билетов проданное на сектор B: '))
#     c = int(input('Введите количество билетов проданное на сектор C: '))
#     print(f'Общая сумма доходов составляет {(a*20)+(b*15)+(c*10)}')
#
# stadium()

# remont

# def remont():
#     kvadratura = int(input('Введите кол-во квадратных метров, необходимых для работы: '))
#     price = int(input('Введите стоимость 5 литровой краски: '))
#     print(f'Необходимо {kvadratura*0.5} литров краски')
#     print(f'Необбходимо {kvadratura*0.8} часов работы')
#     print(f'Краска стоит {(kvadratura*0.5)*(price/5)} гривен')
#     print(f'Стоимость работы стоит {(kvadratura*200)} гривен')
#     print(f'общая стоимость составляет {((kvadratura*0.5)*(price/5))+(kvadratura*200)}')
#
# remont()
#
# def futy_duym():
#     futs = int(input('Введите количество футов'))
#     print(f'{futs} фута(-ов) равняется {futs*12} дюймам')
#
# futy_duym()

# math resr
# def test():
#     congratulation = ['Поздравляю!', 'Идеально!', 'Отлично!', 'Умница!', 'Так держать!']
#     lose = ['Попробуй еще раз!', 'Соберись!', 'Ничего страшного!']
#     while True:
#         a = random.randint(1, 1000)
#         b = random.randint(1, 1000)
#         sum = a + b
#         print(f'{a} + {b} = ')
#         answear = int(input())
#         if answear == sum:
#             print(congratulation[random.randint(0, len(congratulation))])
#         else:
#             i = 0
#             while i <= 3:
#                 print(f'К сожалению неправильно( {lose[random.randint(0, len(lose))]}')
#                 i += 1
#                 print(f'{a} + {b} = ')
#                 answear_try = int(input())
#                 # print(i)
#                 if answear_try == sum:
#                     print(congratulation[random.randint(0, len(congratulation))])
#                     break
#                 if i == 3:
#
#                     print(f'Не огорчайся! Давай решим следующий пример!')
#
# test()

# test_pro


# def plus():
#     congratulation = ['Поздравляю!', 'Идеально!', 'Отлично!', 'Умница!', 'Так держать!']
#     lose = ['Попробуй еще раз!', 'Соберись!', 'Ничего страшного!']
#     while True:
#         a = random.randint(1, 1000)
#         b = random.randint(1, 1000)
#         sum = a + b
#         print(f'{a} + {b} = ')
#         answear = int(input())
#         if answear == sum:
#             print(congratulation[random.randint(0, len(congratulation)-1)])
#         elif answear == 2:
#             proizvedeniye()
#         else:
#             i = 0
#             while i <= 3:
#                 print(f'К сожалению неправильно( {lose[random.randint(0, len(lose)-1)]}')
#                 i += 1
#                 print(f'{a} + {b} = ')
#                 answear_try = int(input())
#                 # print(i)
#                 if answear_try == sum:
#                     print(congratulation[random.randint(0, len(congratulation)-1)])
#                     break
#                 elif answear_try == 2:
#                     proizvedeniye()
#                 elif i == 3:
#                     print(f'Не огорчайся! Давай решим следующий пример!')

# def proizvedeniye():
#     congratulation = ['Поздравляю!', 'Идеально!', 'Отлично!', 'Умница!', 'Так держать!']
#     lose = ['Попробуй еще раз!', 'Соберись!', 'Ничего страшного!']
#     while True:
#         a = random.randint(0,30)
#         b = random.randint(0, 30)
#         sum = a * b
#         print(f'{a} * {b} = ')
#         answear = int(input())
#         if answear == sum:
#             print(congratulation[random.randint(0, len(congratulation)-1)])
#         elif answear == 1:
#             plus()
#         else:
#             i = 0
#             while i <= 3:
#                 print(f'К сожалению неправильно( {lose[random.randint(0, len(lose)-1)]}')
#                 i += 1
#                 print(f'{a} * {b} = ')
#                 answear_try = int(input())
#                 # print(i)
#                 if answear_try == sum:
#                     print(congratulation[random.randint(0, len(congratulation)-1)])
#                     break
#                 elif answear_try == 1:
#                     plus()
#                 elif i == 3:
#                     print(f'Не огорчайся! Давай решим следующий пример!')


# print('В любой момент можно поменять задачу, написав "1" - сложение или "2" - умножение"')
# type = int(input('Введите однно из цифр \n1 - сложение\n2 - умножение\n'))
# if type == 1:
#     plus()
# elif type == 2:
#     proizvedeniye()
# else:
#     print('Введенно невернный ответ')


# average
#
# def first():
#     list = []
#     print('Чтобы прекратить вводить значения введите 112')
#     while True:
#         a = int(input('Введите оценку: '))
#         if a == 112:
#             break
#         else:
#             list.append(a)
#     # print(list)
#     sum = 0
#     for i in list:
#         sum += i
#     average_point = sum/len(list)
#     print(f'Средний бал = {average_point}')
#
# def second():
#     b = int(input('Введите средний бал: '))
#     if b <= 60:
#         print(f'Это уровень F со средним балом {b}')
#     if b > 60 and b < 70:
#         print(f'Это уровень D со средним балом {b}')
#     if b > 69 and b < 80:
#         print(f'Это уровень C со средним балом {b}')
#     if b > 79 and b < 90:
#         print(f'Это уровень B со средним балом {b}')
#     if b > 89:
#         print(f'Это уровень A со средним балом {b}')
#
# def third():
#     first()
#     # b = average_point
#     second()
#
# zadacha = int(input('Что желаете сделать?\n1 - посчитать средний бал\n2 - определить уровень ученика, исходя из бала\n3 - и то и другое'))
# if zadacha == 1:
#     first()
# elif zadacha == 2:
#     second()
# elif zadacha == 3:
#     third()