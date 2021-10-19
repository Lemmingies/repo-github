#Урок №1. Задание №1
print('Задание №1')

# 1 минута
one_minute = 60
# 1 час
one_hour = 3600
# 1 день
one_day = 86400

#Пользователь вводит продолжительность duration в секундах:
duration = int (input('Укажите продолжительность в секундах: '))

#Вывод информации (минута):
if duration<one_minute:
    print ('{} сек'.format(duration))
#Вывод информации (час):
elif one_minute <= duration and one_hour > duration:
    my_minute = duration//one_minute
    my_second = duration%one_minute
    print ('{} мин {} сек'.format(my_minute,my_second));
#Вывод информации (сутки):
elif duration >= one_hour and duration < one_day:
    my_hour = duration // one_hour
    duration = duration % one_hour
    my_minute = duration // one_minute
    my_second = duration % one_minute
    print ('{} час {} мин {} сек'.format(my_hour,my_minute,my_second));