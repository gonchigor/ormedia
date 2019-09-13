'''
Даны три числа. Вывести на экран “yes”, если можно взять какие-то два из них 
и в сумме получить третье;
'''

num1 = int(input("Введите первое число"))
num2 = int(input("Введите второе число"))
num3 = int(input("Введите третье число"))

if num1 + num3 == num2 or num1 + num2 == num3 or num1 + num2 == num3:
    print('yes')
else:
    print("ERROR")
