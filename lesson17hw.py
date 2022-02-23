import random
def restaurant():
    time = input('Доброрго времени суток. На которое время желаете забронировать столик? ')
    visitors = int(input('Введите количество людей за столиком: '))
    visitors_list = []
    visitors_pizza = []
    visitors_size = []
    for i in range(visitors):
        a = f'Посетитель номер {i+1}'
        visitors_list.append(a)
    for i in visitors_list:
        pizza_type = input(f'Введите название пиццы для "{i}": ')
        pizza_size = int(input(f'Введите длину пиццы {pizza_type.title()} в сантиметрах: '))
        visitors_pizza.append(pizza_type)
        visitors_size.append(pizza_size)
    # print(visitors_offers)
    # print(visitors_list)
    print('Проверьте данные!\n')
    i = 0
    print(f'Ожидаем вас в {time}')
    print(f'За столиком номер {random.randint(1,30)}')
    print(f'Разчитаный на {len(visitors_list)} мест(-а)')
    while i <= len(visitors_list):
        print(f'{visitors_list[i]} Заказал пиццу {visitors_pizza[i]} размером {visitors_size[i]}')
        i += 1



restaurant()