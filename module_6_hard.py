import math

class Figure:
    side_count = 0

    def get_color(self, color, sides):
        self.__sides = sides
        self.__color = color
        self.filled = False
        if self.__sides != self.sides_count:
            self.__sides = [sides.__sides] * self.side_count


    def __is_valid_color(self, r, g, b):
        self.r, self.g, self.b = r, g, b
        if 0 <= self.r <= 255 and 0 <= self.g <= 255 and 0 <= self.b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [self.r, self.g, self.b]

    def __is_valid_sides(self, *sides):
        for side in sides:
            if side > 0 and side == self.__sides:
                self.filled = True

    def get_sides(self):
        return list(self.__sides)

        # for side in self.sides:
        #     if len(self.sides) == self.sides_count and side > 0 and type(side) == int:
        #         return True
        #     else:
        #         return False



    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = new_sides

    def __len__(self):
        return sum(self.__sides)



class Circle(Figure):
    sides_count = 1

    def __init__(self, color, side):
        super().__init__(color, side)
        self.radius = self.radius()

    @staticmethod
    def radius(length):
        return length / (2 * math.pi)

    def get_square(self):
        # radius = self.get_sides()[0]  # Получаем радиус из сторон
        self.radius = self.get_sides()[0] / (2 * math.pi)
        return math.pi * (self.radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        p = self.__len__() / 2
        return math.sqrt(p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2]))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.sides = [self.get_sides()[0]] * 12


    def get_volume(self):
        side_length = self.get_sides()[0]  # Получаем длину стороны
        return side_length ** 3

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
