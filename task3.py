# 3) Реализовать функцию my_func(), 
# которая принимает три позиционных аргумента, 
# и возвращает сумму наибольших двух аргументов.


def sum_largest_arguments(arg_1, arg_2, arg_3):
    my_list = sorted([arg_1, arg_2, arg_3])
    print(f'Сумма наибольших двух аргументов = {my_list[1] + my_list[2]}')

number_1 = int(input('1 аргумент: '))
number_2 = int(input('2 аргумент: '))
number_3 = int(input('3 аргумент: '))

sum_largest_arguments(number_1, number_2, number_3)