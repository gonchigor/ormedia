import math
'''
Создайте класс Triangle с методом area, подсчитывающим и возвращающим площадь
треугольника. Затем создайте объект Triangle, вызовите в нем area и
выведите результат
'''


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = 0.5 * (self.a + self.b + self.c)
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


def main():
    a = float(input('a='))
    b = float(input('b='))
    c = float(input('c='))
    triangle = Triangle(a, b, c)
    print(triangle.area())


if __name__ == '__main__':
    main()
