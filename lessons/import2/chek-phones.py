def check_phone(phone_number):
    correct_lengh = 10

    return len(phone_number) == correct_lengh

def get_operator(phone_number):
    operator_K = ('067', '097')
    operator_V = ('050', '066', '099')
    operator_L = ('063', '093', '073')
    
    code = phone_number[0:3]

    if code in operator_K:
        return 'K'
    elif code in operator_V:
        return 'V'
    elif code in operator_L:        
        return 'L' 
    else:
        return None


fn = 'D:\goiteens\lessons\import2\phones.txt'
file_K = 'D:\goiteens\lessons\import2\phones-K.txt'
file_V = 'D:\goiteens\lessons\import2\phones-V.txt'
file_L = 'D:\goiteens\lessons\import2\phones-L.txt'


K_file = open(file_K, 'w')
V_file = open(file_V, 'w')
L_file = open(file_L, 'w')

files = {
    'K': file_K,
    'L': file_L,
    'V': file_L}
with open(fn, 'r') as f:
    while True:
        phone = f.readline()
        if not phone:
            break

        phone = phone.rstrip('\n')
        print(phone)
        if (check_phone(phone) == True):
            #check_operator
            operator_code = get_operator(phone)
            if (operator_code):
                current_file = files[operator_code]
                current_file.write(phone + '\n')
            else:
                print('operator not supported', phone)
        else:
            print('phone is invalid', phone)



K_file.close()
V_file.close()
L_file.close()