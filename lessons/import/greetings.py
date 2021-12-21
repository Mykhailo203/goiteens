def good_morning(name):
    print('good morning', name)

def good_afternoon(name):
    print('good afternoon', name)

def good_evening(name):
    print('good evening', name)


def say_hello(name):
    print(f'Hello {name}')


def file_import():
    print("You imported greetings")
    

def file_run():
    print("greetings run")
    

if __name__ == '__main__':
    file_run()
else:
    file_import()