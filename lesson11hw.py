# ex 6.1

# info = {
#     "first_name": "Jack",
#     "last_name": "Figgurdson",
#     "age": 17,
#     "city": "Kharkiv"
# }
# for i, g in info.items():
#     print(f'Ключ: {i}.\nЗначение: {g}\n\n')

# ex 6.2

# import random
# from random import randint

# voc = {
#     'nick': '',
#     'vanya': '',
#     'zhenya': '',
#     'oleg': '',
#     'dima': ''
# }
# for i in voc.keys():
#     voc[f'{i}'] = randint(0, 9)
# print(voc)

# ex 6.2(недоделаное)

# names = ['gleb', 'den', 'nick', 'jack', 'liza']
# i = 0
# chisla = []
# while i < len(names):
#     n = randint(0, 9)
#     chisla.append(n)
#     i += 1
# print(names)
# print(chisla)
# voc = {}
# abc = 1
# for a in names:
#     voc[{i}] = chisla[abc]
#     abc += 1
# print(voc)

# ex 6.3

# voc = {
#     'Логический - ': 'может принимать одно из двух значений — True (истина) или False (ложь).',
#     'Числа -': 'могут быть целыми (1 и 2), с плавающей точкой (1.1 и 1.2), дробными (1/2 и 2/3), и даже комплексными.',
#     'Строки -': 'последовательности символов Юникода, например, HTML-документ.',
#     'Списки -': 'упорядоченные последовательности значений.',
#     'Кортежи -': 'упорядоченные неизменяемые последовательности значений.', }
# print('Типы данных Python:\n')
# for i,g in voc.items():
#     print(f'{i}\n{g}\n\n')

# ex 6.4
# прошлое задание я выполнил так как это

# ex 6.5
# voc = {
#     'nile': 'egypt',
#     'dnepr': 'ukraine',
#     'amazonka': 'brazilia'
# }
# for i, g in voc.items():
#     print(f'The {i.title()} runs through {g.title()}')
# for a in voc.keys():
#     print(a.title())
# for b in voc.values():
#     print(b.title())

# voc = {
#     'lyuda': 'complete',
#     'nika': 'no',
#     'sveta': 'complete',
#     'gleb': 'no',
#     'nick': 'complete',
#     'nastya': 'no'
# }
# for i,g in voc.items():
#     if g == 'complete':
#         print(f'Поздравляю, {i.title()}! Вы успешно зпрегистрировались')
#     else:
#         print(f'Уважаемый(-ая), {i.title()}, прошу зарегистрироваться!')