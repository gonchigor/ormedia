'''
Задание 1: Определите класс Apple с четырьмя переменными экземпляра,
представляющими четыре свойства яблока.
'''


class Apple:
    def __init__(self, radius, color, variety, moll=0):
        self.radius = radius
        self.color = color
        self.variety = variety
        self.moll = moll


def main():
    apple = Apple(10, 'yellow', 'антоновка')
    print(apple.radius)
    print(apple.color)
    print(apple.variety)
    print(apple.moll)


if __name__ == '__main__':
    main()
