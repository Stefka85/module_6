import math

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color
        self.filled = False
        if len(sides) == self.sides_count:
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count  # Инициализация единичными сторонами

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        for side in sides:
            if len(sides) == self.sides_count and isinstance(side, int) and side > 0:
                return True
            else:
                return False

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.radius = self.get_sides()[0]  # Устанавливаем радиус

    def get_square(self):
        return math.pi * (self.radius ** 2)

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        self.radius = self.get_sides()[0]  # Обновляем радиус


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length):
        super().__init__(color)
        self.set_sides(*[side_length] * self.sides_count)
        # self.__sides = [self.get_sides()[0]] * 12  # Все 12 рёбер имеют одинаковую длину

    def get_volume(self):
        return self.get_sides()[0] ** 3  # Объём куба

    # def __init__(self, color=[0, 0, 0], side_length=1, filled=False):
    #     sides = [side_length] * 12
    #     super().__init__(color, sides, filled=filled)

    # def get_volume(self):
    #     side_length = self.get_sides()[0]  # Получаем длину стороны
    #     return side_length ** 3


if __name__ == '__main__':
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
