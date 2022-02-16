# ex 8.1

# def display_message():
#     r = f'Эта глава про многочисленные победы'
#     return r
# result = display_message()
# print(result)

# ex 8.2

# title = input('Введите название книги ')
# def favourite_book(title):
#     r = f'One of my favourite books is {title}'
#     return r
# result = favourite_book(title)
# print(result)

# ex 8.3

# def make_shirt(size, text):
#     r = f'Я заказываю футболку размером {size}. Текст, который необходимый на футболке: {text}'
#     return r
# x = input('Введите размер: ')
# y = input('Введите желаемый теккст: ')
# print(make_shirt(x, y))

# ex 8.4

# def make_shirt(size, text):
#     r = f'Я заказываю футболку размером L. Текст, который необходимый на футболке: I love Python\n'
#     r += f'Я заказываю футболку размером {size}. Текст, который необходимый на футболке: {text}'
#     return r


# x = input('Введите размер второй футболки: ')
# y = input('Введите желаемый теккст на второй футболке: ')
# print(make_shirt(x, y))

# ex 8.5

des = {
    'kharkiv': 'describe 1',
    'kyiv': 'describe 2',
    'lviv': 'describe 3'
}
def describe_city(x, y):
    print(f'Выбранный город: {x}\nЕго описание: {y}')
for i, g in des.items():
    describe_city(i,g)