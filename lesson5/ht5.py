'''
Создайте классы Rectangle и Square с методом calculate_perimeter,
вычисляющим периметр фигур, которые эти классы представляют.
Создайте объекты Rectangle и Square вызовите в них этот метод.

В классе Square определите метод change_size,
позволяющий передавать ему число, которое увеличивает или
уменьшает (если оно отрицательное) каждую сторону объекта Square
на соответствующее значение
'''


class Square:
    def __init__(self, a):
        self.a = a

    def calculate_perimetr(self):
        return 4 * self.a

    def change_size(self, change):
        self.a += change


class Rectangle(Square):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def calculate_perimetr(self):
        return 2 * (self.a + self.b)


def main():
    rectangle = Rectangle(7, 15)
    square = Square(5)
    print('Rectangle:', rectangle.calculate_perimetr())
    print('Square:', square.calculate_perimetr())
    square.change_size(-2)
    print('New square:', square.calculate_perimetr())


if __name__ == '__main__':
    main()
