booking_list = list()
surname1 = input('Enter surname')
how_many_people = input('How many people will be in the restourant')
def booking(surname, people=2):
    global booking_list
    booking_list.append([surname, people])
    print('You booked places for', people, 'people in restourant')
booking(surname1)
booking(surname1, how_many_people)