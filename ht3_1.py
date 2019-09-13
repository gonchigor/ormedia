"""
Даны три числа. Вывести на экран “yes”, если среди них есть одинаковые, иначе вывести “ERROR”
"""

num1 = int(input("Введите первое число"))
num2 = int(input("Введите второе число"))
num3 = int(input("Введите третье число"))

if num1 == num2 or num1 == num3 or num2 == num3:
    print('yes')
else:
    print("ERROR")
