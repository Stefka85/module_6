import math

class Figure:
    side_count = 0

    def get_color(self, color, sides, filled = False):
        self.__color = color
        self.__sides = sides
        self.filled = filled

    def __is_valid_color(self, r, g, b):
        self.r, self.g, self.b = r, g, b
        if 0 <= self.r <= 255 and 0 <= self.g <= 255 and 0 <= self.b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self.color = [self.r, self.g, self.b]


    def get_sides(self, *args):
        for side in self.sides:
            if len(self.sides) == self.sides_count and side > 0 and type(side) == int:
                return True
            else:
                return False

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides

    def __len__(self):
        return sum(self.__sides)



class Circle(Figure):
    sides_count = 1

    def __init__(self, color=[0, 0, 0], radius = 0, filled = False):
        super().__init__(color, radius, filled)

    def get_square(self):
        radius = self.get_sides()[0]  # Получаем радиус из сторон
        return math.pi * (radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color = [0, 0, 0], sides = [0, 0, 0], filled = False):
        super().__init__(color, sides, filled)

    def get_square(self):
        p = self.__len__() / 2
        return math.sqrt(p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2]))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color=[0, 0, 0], side_length=1, filled=False):
        sides = [side_length] * 12
        super().__init__(color, sides, filled=filled)

    def get_volume(self):
        side_length = self.get_sides()[0]  # Получаем длину стороны
        return side_length ** 3

if __name__ == "__main__":
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

    # Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
print(len(circle1))

    # Проверка объёма (куба):
print(cube1.get_volume())