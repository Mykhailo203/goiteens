import csv, os


# https://docs.python.org/3/library/csv.html
# https://www.pythontutorial.net/python-basics/python-write-csv-file/

source_file = 'pupils.csv'


headers = ['name', 'city'] 

data_one_row = ['Dima', 'Kyiv']
data_many_rows = [
    ['Dima', 'Kyiv'],
    ['Inna', 'Odesa'],
    ['Ivan', 'Dnipro'],
    ['Ulyana', 'Kharkiv'],
]    

with open(source_file, 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerow(data_one_row)

    writer.writerows(data_many_rows)

new_data = dict()
new_data['name'] = 'Oleh'
new_data['city'] = 'Kyiv'

with open(source_file, 'a', encoding='UTF8', newline='') as file:
    writer_dict = csv.DictWriter(file, headers)
    writer_dict.writerow(new_data)
    writer_dict.writerow({'name': 'Ihor', 'city': 'Vinnytsya'})


with open(source_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['name'], row['city'])    


print(os.getcwd())
print(os.path.abspath("pupils.csv"))