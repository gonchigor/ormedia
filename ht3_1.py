"""
Даны три числа. Вывести на экран “yes”, если среди них есть одинаковые, иначе вывести “ERROR”
"""

num1 = int(input("Введите первое число"))
num2 = int(input("Введите второе число"))
num3 = int(input("Введите третье число"))

def equals(*args):
    for i in range(0, len(args) - 1):
        for j in range(i + 1, len(args)):
            if args[j] == args[i]:
                return 'yes'
    return 'ERROR'

# if num1 == num2 or num1 == num3 or num2 == num3:
#     print('yes')
# else:
#     print("ERROR")

print(equals(num1, num2, num3))
