#Урок №1. Задание №2
print('Задание №2')

#1. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!

cubes = [x**3 for x in range (100) if  x%2 != 0 ]
print('Cоздан список кубов нечётных чисел {}'.format(cubes))
my_numbers_sum = 0
my_numbers_sum_list=[]

#Итерация идет по списку
for i in range(len(cubes)):
    my_str = str(cubes[i])
    my_list = list(my_str)
    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])
    #Вычислить сумму чисел

    #Сумма чисел делится нацело на 7
    if my_numbers_sum % 7 == 0:
        print('Cумму чисел, делящихся на 7: ',my_numbers_sum)
        my_numbers_sum_list.append(my_numbers_sum)

print('Список чисел, делящихся на 7 (задание 1): ',my_numbers_sum_list)

#2. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.

cubes = [(x**3)+17 for x in range(100) if x%2 == 0]
print('Cоздан список кубов нечётных чисел {}'.format(cubes))
my_numbers_sum = 0
my_numbers_sum_list_even_numbers =[]

#Итерация идет по списку:
for i in range(len(cubes)):
    my_str = str(cubes[i])
    my_list = list(my_str)
    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])
    #Вычислить сумму чисел

    #Сумма чисел делится нацело на 7
    if my_numbers_sum % 7 == 0:
        print('Cумму чисел, делящихся на 7: ',my_numbers_sum)
        my_numbers_sum_list_even_numbers.append(my_numbers_sum)

print('Список чисел, делящихся на 7 (задание 2): ',my_numbers_sum_list_even_numbers)

#* Решить задачу под пунктом b, не создавая новый список.
