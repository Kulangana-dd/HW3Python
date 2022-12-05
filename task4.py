# 4) Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора *.
# Второй — более сложная реализация без оператора *, предусматривающая использование цикла.

def number_power(x, y):
    if int(y) < 0 < float(x):
        print(f'Число {x} в степени {y} = {x ** y}')
    else:
        print('Введите значения в соответствии с заданием')
  
number_1 = int(input('Введите первое положительное число: '))
number_2 = int(input('Введите второе отрицательное число: '))

number_power(number_1, number_2)