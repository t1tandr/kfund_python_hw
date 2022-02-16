# ex 8.6

# city = {
#     'santiago': 'chile',
#     'kyiv': 'ukraine',
#     'warszawa': 'poland',
# }
# def city_func(x, y):
#     print(f'{x.title()}, {y.title()}')
# for i,g in city.items():
#     city_func(i,g)

# ex 8.7, 8.8 (associations)
album = {}
def make_album(x,y):
    album[f'{x}'] = f'{y}'
    print(album)
    for i,g in album.items():
        print(f'Исполнитель: {i}\nАльюом: {g}')
    print("Если хотите перестать добавлять введите 'stop'")

# x = input('Введите исполнителя: ')
# y = input('Введите название альбома: ')
while True:
    x = input('Введите исполнителя: ')
    y = input('Введите название альбома: ')
    if x == 'stop' or y == 'stop':
        break
    else:
        make_album(x,y)


