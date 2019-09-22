'''
Распечатывать дни недели с их порядковыми номерами.
Кроме того, рядом выводить выходной ли это день или рабочий.
'''

week_days = [
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенье",
    ]


def get_day(i):
    worker = 'рабочий' if i <= 4 else 'выходной'
    return (i+1, week_days[i], worker)


# i=1
# for day in week_days:
#     print(i, day, end=" ")
#     if i <= 5:
#         print("рабочий")
#     else:
#         print("выходной")
#     i+=1

for i in range(7):
    print('{} {} {}'.format(*get_day(i)))
