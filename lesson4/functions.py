# Пустая функция
def func():
    pass

# Написать функцию, которая принимает число, возвращает его значение умноженное на два.
def func2(x):
    return x * 2

# Напишем функцию, которая определяет параметр на чётность. 
# Если чётное число принтим (‘yes’) в ином случае (‘no’).
def odd_ch(x):
    if x % 2:
        print('no')
    else:
        print('yes')

#Пишем функцию, принимающую два аргумента. 
# После чего проверим, если первое число больше 10, принтим (‘да’). 
# Если меньше(‘нет’).
def two_args(a,b):
    if a > 10:
        print('да')
    elif a < 10:
        print('нет')

# print(odd_ch(4))

# Написать лямбда функцию, которая делит по модулю(%) два аргумента.
f = lambda x, y: x % y

print(f(7,3))

# Создадим функцию с простыми командами. 
# Обернём её в декоратор, который бы дополнял возможности функции.

def decorator(func):
    def wrap():
        print("=======")
        func()
        print('=======')
    return wrap


@decorator
def say_hello():
    print(5*3)
    
    
say_hello()

# Использовать функцию map и filter 
array = [4, 6, 78, 3, 56]
print(list(map(lambda x: x ** 2, array)))
print(list(filter(lambda x: x > 10, array)))

# Создадим чистую и нечистую функцию.
def clean_func(a,b):
    return 2 * a + 3 * b


def not_clean_func():
    array.append(8) 
    
# Сделать функцию поиска минимума и максимума в списке.
def search_min_max(l):
    min_l = l[0]
    max_l = l[0]
    for el in l:
        if el < min_l:
            min_l = el
        if el > max_l:
            max_l = el
    return min_l, max_l

print(search_min_max(array))

# Написать функцию, которая определяет, является ли год високосным.
#  Пользователь вводит год, если он високосный, то функция возвращает True. 
# Если нет, то False.
def visok(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print(visok(1900))

# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), 
# и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
def season(month):
    if month in (12, 1, 2):
        return 'зима'
    elif month in (3, 4, 5):
        return 'весна'
    elif month in (6, 7, 8):
        return 'лето'
    elif month in (9, 10, 11):
        return 'осень'
    
print(season(2))
# Написать функцию date, принимающую 3 аргумента — день, месяц и год.
#  Вернуть True, если такая дата есть в нашем календаре, и False иначе

def date(day, month, year):
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    elif day == 31 and month not in (1, 3, 5, 7, 8, 10, 12):
        return False
    elif day == 30 and month == 2:
        return False
    elif day == 29 and month == 2:
        return visok(year)
    return True

print(date(29, 2, 1996))


# Список [16, -17, 2, 78.7, False, False, {‘True’: True}, 555, 12, 23, 42, ‘DD’] 
# Функция, принимает на вход список -выбирает из него все int и float -составить из 
# него новый список, отсортированный от наименьшего значения большему.

input_list = [16, -17, 2, 78.7, False, False, {'True': True}, 555, 12, 23, 42, 'DD']
def list_func(list_):
    li = filter(lambda x: type(x) in (int, float), list_)
    li = list(li)
    li.sort()
    return li

print(list_func(input_list)) 