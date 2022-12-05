# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list_numbers = [2, 3, 5, 9, 3]
odd_positions = []
sum_result = 0
for i in range(len(list_numbers)):
    if i % 2 != 0:
        odd_positions.append(list_numbers[i])

print(list_numbers)
print(f'Элементы на нечётных позициях: {odd_positions} \nCумма: {sum(odd_positions)}')