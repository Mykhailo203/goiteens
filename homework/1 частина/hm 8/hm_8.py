def sum(a, b):
    return a + b


def sub(a, b):
    return a - b

def dil(a, b):
    error_message = 'На нуль ділити не можна'
    if b == 0:
        return error_message
    else:
        return a / b

def multiplication(a, b):
    return a * b

def stepin(a, b):
    return a ** b

def chek_operation(operation):
    return operation in ['+', '-', '/', '*', '**']

def calculate(operand_a, operand_b, operation):
    result = None

    if operation == '+':
        result = sum(operand_a, operand_b)
    elif operation == '-':
        result = sub(operand_a, operand_b)
    elif operation == '/':
        result = dil(operand_a, operand_b)
    elif operation == '*':
        result = multiplication(operand_a, operand_b)
    elif operation == '**':
        result = multiplication(operand_a, operand_b)
    print(operand_a, operation, operand_b, '=', result)



a, user_input_operation, b = input('Enter:').split()

if not chek_operation(user_input_operation):
    print('Operation', user_input_operation, 'not supported yet')
else:
    calculate(int(a), int(b), user_input_operation )

    
    