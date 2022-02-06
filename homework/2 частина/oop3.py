from math import pi


class Figure:
    _title = ""
    _area = 0.0
    
class Foursquare(Figure):
    def __init__(self, side=0, title="foursquare"):
        self._title = title
        self._side = side

    def get_side(self):
        return self._side
        
    def set_side(self, side):
        if not isinstance(self._side, int):
            raise TypeError("Довжина сторони має бути числом.")
        else:
            self._side = side
    p = property(get_side, set_side)
    def count_area(self):
        self._area = self._side * self._side

    def __repr__(self):
        return f"Фігура квадрат має площу {self._area} см квадратних"


class Circle(Figure):
    from math import pi
    def __init__(self, radius, title="circle"):
        self._title = title
        self._radius = radius

    def get_radius(self):
        return self._radius
    
    def set_radius(self, radius):
        if not isinstance(self._radius, int):
            raise TypeError("Радіус має бути числом.")
        else:
            self._radius = radius

    p = property(get_radius, set_radius)
    def count_area(self):
        self._area = self._radius**2 * pi

    def __repr__(self):
        return f"Фігура коло має площу {self._area} см квадратних"



figure1 = Foursquare(13)
figure1.p = 11
figure1.count_area()
print(figure1)

figure2 = Circle(23)
figure2.p = 9
figure2.count_area()
print(figure2)