#генерація данних для прямої
#y(x) = k*x + b

def generate_line_data(x_left_interval, step, points_count, coef):
    k = coef[0]
    b = coef[1]

    x = list()
    y = list()

    for points_number in range(0, points_count):
        point_x = x_left_interval + step * points_number
        point_y = k*point_x + b

        x.append(point_x)
        y.append(point_y)

    print(x)
    print(y)
    return{'x_data':x, 'y_data':y}

generate_line_data(3, 2, 8, [2, 7])
generate_line_data(-5, 1, 10, [2, 3])




# генеруємо дані для параболи
# y(x) = a*x^2 + b
def generate_parabola_data(x_left_intervsl, step, points_count, coef):
    a = coef[0]
    b = coef[1]

    x = list()
    y = list()

    for point_number in range(0, points_count):
        point_x = x_left_intervsl + step * point_number
        point_y = a * point_x ** 2 + b

        x.append(point_x)
        y.append(point_y)
    
    return {'x_data': x, 'y_data': y}
if __name__=='__main__':
    generate_line_data(3, 2, 8, [2, 7])
    generate_line_data(-5, 1, 10, [2, 3])
