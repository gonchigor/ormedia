class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
        print('Создано')

    def rot(self, days, temp):
        self.mold = days * temp


or1 = Orange(10, 'dark orange')
print(or1)
or1.weight = 228
or1.color = 'pink orange'
print(or1.weight)
print(or1.color)

or2 = Orange(12, 'black orange')
or3 = Orange(23, 'white orange')
or4 = Orange(5, 'red orange')

orange = Orange(6, 'pickle')
orange.rot(10, 33)
print(orange.mold)
