# zadacha 1

# names = ['zhenya', 'vanya', 'nikita']
# for i in names:
#     print(f'Приветствую, {i.title()}!')

# zadacha 2

# transport = ['car', 'motorcycle', 'bike']
# for a in transport:
#     print(f'I want to buy a {a}')

# zadacha 3

# years_list = [2004, 2005, 2006, 2007, 2008, 2009]
# year3 = years_list[3]
# print(f'3 года мне исполнилось в {year3} году')

# years_list.append(2010)
# print(f'Больше всего лет мне было в {years_list[-1]} году')

# 4 zadacha

# things = ['wallet', 'mirror', 'umbrella']
# print(things[-1])
# print(things)
# print(things[-1].upper())
# print(things)
# del things[-1]
# print(things)

# 5 zadacha

# languages = ['Georgian', 'Estonian', 'Ukrainian']
# print(languages[-1].lower())
# languages.reverse()
# print(languages)
# print(languages[-1].upper())

# 6 zadacha

# 7 zadacha

# languages = ['Ukrainian', 'French', 'Bulgarian', 'Norwegian', 'Latvian']
# languages.sort(reverse=True)
# print(languages)
# print(sorted(languages))
# languages.reverse()
# print(languages)

# 8 zadacha

# s = input('Ведите числа')
# a =[]
# for i in s:
#     if i != ' ':
#         b = int(i)
#         a.append(b)
# summ = 0
# for g in a:
#     summ += g
# print(summ)

#  9 zadacha

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# summ = 0
# for i in a:
#     if i > 5:
#         print(i)

# 10 zadacha

year = 2004
years = []
while year <= 2022:
    years.append(year)
    year += 1
print(years)


