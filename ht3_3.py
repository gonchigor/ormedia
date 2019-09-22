'''
Посчитать сумму числового ряда от 0 до 14 включительно. Например, 0+1+2+3+…+14;
'''

def sum_r(n):
    s = 0
    for i in range(n+1):
        s += i
    return s


# sum = 0
# for i in range(0,15):
#     sum += i
# print(sum)

print(sum_r(14))
