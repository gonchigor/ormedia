'''
Даны три числа. Вывести на экран “yes”, если можно взять какие-то два из них 
и в сумме получить третье;
'''
def sum_equal(*args):
    # TODO: work with 3 numbers. Fix it for n numbers
    for i in range(0, len(args) - 1):
        for j in range(i + 1, len(args)):
            s = args[i] + args[j]
            if args.count(s):
                return 'yes'
    return 'ERROR'

num1 = int(input("Введите первое число"))
num2 = int(input("Введите второе число"))
num3 = int(input("Введите третье число"))

# if num1 + num3 == num2 or num1 + num2 == num3 or num1 + num2 == num3:
#     print('yes')
# else:
#     print("ERROR")

print(sum_equal(num1, num2, num3))