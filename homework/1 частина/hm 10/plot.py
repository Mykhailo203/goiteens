import matplotlib.pyplot as plt
import generate_data as gd

#data = gd.generate_line_data(0, 1, 25, [2, 8])


data = gd.generate_parabola_data(-5, 1, 11, [2, 8])


plt.plot(data['x_data'], data['y_data'])
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()

plt.show()