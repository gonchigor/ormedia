'''
1. Создать переменную со строковым типом данных 
2. Срезать элементы
3. Создать кортеж
3. Записать туда срез
4. Достать элемент из кортежа
'''

s = 'Hello, world'
print(s)
s_elements = s[3:7]
print(s_elements)
# s_tuple = tuple()
# s_tuple = tuple(s_elements)
n_tuple = (1,2, s_elements, '554')
# print(s_tuple)
# element = s_tuple[2]
# print(element)
print()
print(n_tuple)
print(n_tuple[2])

my_dict = {
    'Queen': 'Bohemian Rhapsody',
    'Beetles': 'Yellow Submarine',
    'ДДТ': 'Последняя осень'
}

print(my_dict)
print(my_dict['ДДТ'])
# print(__doc__)