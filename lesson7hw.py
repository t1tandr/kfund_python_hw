# task1

# friends = ['nick', 'andrey', 'ivan', 'igor']
# for i in friends:
#     print(i)

# task 2
# friends = ['nick', 'andrey', 'ivan', 'igor']
# for i in friends:
#     print(f'Привет! {i.title()}')


# task 3
# car = ['mazda', 'renault', 'bmw']
# for i in car:
#     print(f'Я бы хотеле машину марки {i.title()}')

# task 4
# invite = ['igor', 'ivan', 'tanya', 'sonya']
# for i in invite:
#     print(f'Привет, {i}, я бы хотел пригласить тебя на мою вечеринку!')

# task 5
# invite = ['igor', 'ivan', 'tanya', 'sonya']
# invite.remove('tanya')
# for i in invite:
#     print(f'Привет, {i.title()}, я бы хотел пригласить тебя на мою вечеринку!')

# task 6
invite = ['igor', 'ivan', 'tanya', 'sonya']
invite.remove('tanya')
invite.insert(0, 'kate')
invite.insert(2, 'oleg')
invite.append('zhektor')
for i in invite:
    print(f'Привет, {i.title()}, я бы хотел пригласить тебя на мою вечеринку!')
