transport = {
    'AA1111AA': 'Іванов Іван',
    'IVANOV'  : 'Іванов Іван',
    'AA0007AA': 'Семенов Андрій',
    'AA007AA' : 'Іванов Іван',
    'AВ1111AВ': 'Вінниця Водоканал',
    'AІ1010КК': 'Семенов Андрій',
}

transport['AB1111AA'] = 'Sidorov Sidr'
transport['BH1111AA'] = 'Sidorova Olena'

print(transport)

'''for number, fio in transport.items():
    if number == 'AA0007AA':
        print(fio)
        break
else:
        print('car not found')'''


car_owner = transport.get('AA0007AA1', False)
if car_owner:
    print(car_owner)
else:
        print('car not found')


people = dict()

for car_number, fio in transport.items():
    
    is_present = people.get(fio, False)
    
    if is_present:
        #додаємо ще одну машину
        car_count = people[fio]
        car_count += 1
        people[fio] = car_count
    else:
        people[fio] = 1


for fio, car_count in people.items():
    if car_count > 1:
        print(fio, 'has', car_count, 'cars')