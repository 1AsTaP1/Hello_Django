# Задача 1
# На вход функция more_than_five(lst)
# получает список из целых чисел.
# Результатом работы функции должен стать новый список,
# в котором содержатся только те числа, которые больше 5 по модулю.

# def more_than_five(lst):
#     lst_1 = []
#     for i in lst:
#         if abs(i) > 5:
#             lst_1.append(i)
#     return lst_1
# print(more_than_five([1, 5, 6, -10, -2, -15, 30]))

# Задача 2
# Есть список чисел с дубликатами.
# Создать новый список в котором будут только уникальные элементы.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# print(f'Список без повторяющихся элементов: {list(set(sorted(a + b)))}')
# print(f'Элементы, которые пересекаются: {list(set(a) & set(b))}')

# Задача 3
# Напишите программу для слияния нескольких словарей в один.

# a = {1: 40, 2: 20, 'a': 123}
# b = {'k': 21, 'c': 'b', 22: 'o'}
#Первый способ объединения
# print(a | b)
# Второй способ объединения
# k = a.copy()
# k.update(b)
# print(k)

# Задача 4
# Напишите проверку на то, является ли строка палиндромом.
# Палиндром — это слово или фраза, которые одинаково читаются
# слева направо и справа налево.
# a = str(input("Ввежите строку: "))
# if a != a[::-1]:
#     print("Не является палидромом")
# else:
#     print("Является палидромом")

# Задача 5
# Вы принимаете от пользователя последовательность чисел,
# разделённых запятой. Составьте список и кортеж с этими числами.
# a = input("Введите последовательность чисел через запятую: ")
# print(a.split(","), "\n", tuple(a.split(",")))

# Задача 6
# При заданном целом числе n посчитайте n + nn + nnn.
# a = int(input('Введите 1 число: '))
# b = a + (a + a) + (a + a + a)
# print(b)

# Задача 7
# Напишите программу, которая выводит чётные числа из
# заданного списка и останавливается, если встречает число 237.
# (список numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     ]
# numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823,
#            566, 597, 978, 328, 615, 953, 345,
#            399, 162, 758, 219, 918, 237, 412, 566, 826,
#            248, 866, 950, 626, 949, 687, 217]
# for i in numbers:
#     if i % 2 == 0:
#         print(i)
#     elif i == 237:
#         break


# Задача 8
# Сложите цифры целого семизначного числа.

# a = int(input("Введите целое: "))
# b = 0
# while a != 0:
#     b = b + a % 10
#     a = a // 10
# print(b)

# Задача 9
# Посчитайте, сколько раз символ встречается в строке.

# a = str(input("Введите строку: "))
# b = str(input("Введите символ: "))
# print(f'Количество символов, которую ввели: {a.count(b)}')
# b = {i: a.count(i) for i in a}
# print("Количество каждых символов: ", b)

# Задача 10
# Поменяйте значения переменных местами.
# a = 2
# b = 3
# c = a
# a = b
# b = c
# print(a, b)

# Задача 11
# Нужно проверить, все ли числа в последовательности уникальны.
# from random import *
# N = 10
# a = [0] * N
# for i in range(N):
#     a[i] = int(randint(1, 50))
# print(a)
# for i in range(N-1):
#     for j in range(i+1, N):
#         if a[i] == a[j]:
#             print("Есть одинаковые")
#             exit()
# print("Все элементы уникальны")

# def print_hi(name):
#     print(f'Hi, {name}')
#
# if __name__ == "__main__":
#     print_hi("Pycharm")