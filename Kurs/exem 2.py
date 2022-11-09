# Задача 1
# Добавьте на свой рабочий стол папку, в ней создайте 3 текстовых
# файла: test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
# После этого удалите созданную папку.
# Все операции выполнять с помощью встроенных функций библиотеки os.
# import os
# os.mkdir("C:\\Users\\Admin\\Desktop\\Экзамен")
# os.chdir("C:\\Users\\Admin\\Desktop\\Экзамен")
# Создание файлов
# a = open('C:\\Users\\Admin\\Desktop\\Экзамен\\test_1.txt', 'w')
# b = open('C:\\Users\\Admin\\Desktop\\Экзамен\\test_2.txt', 'w')
# c = open('C:\\Users\\Admin\\Desktop\\Экзамен\\test_3.txt', 'w')
# Переименовывание файлов
# os.rename('test_1.txt', 'rename_1.txt')
# os.rename('test_2.txt', 'rename_2.txt')
# os.rename('test_3.txt', 'rename_3.txt')
# Удаление файлов так как нельзя удалить папку в которой есть файлы
# os.remove('rename_1.txt')
# os.remove('rename_2.txt')
# os.remove('rename_3.txt')
# Удаление папки
# os.rmdir("C:\\Users\\Admin\\Desktop\\Экзамен")
# print(os.getcwd()) # Проверка директории

# Задание 2
# Найти в списке те элементы, значение которых меньше среднего
# арифметического, взятого от всех элементов списка.
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = sum(a)/len(a)
# c = []
# for i in a:
#     if i < b:
#         c.append(i)
# print(c)

# Задание 3
# Создайте 2 множества:
# - Если они одинаковые: вывести что они равны
# - Если 1 множество полностью состоит из второго: вывести сообщение
# множество 1
# состоит из множества2
# - Если 2 множество полностью состоит из 1: вывести сообщение
# множество 2
# состоит из множества 1
# - Если они пересекаются: вывести элементы в которых они пересекаются
# - Если не пересекаются: вывести сообщение об этом
# a = {"a", 2, "b", 4, "c", 6}
# b = {"a", 2, "b", 4, "c", 6}
# if len(a) == len(b):
#     print("Множества равны")
# if a <= b:
#     print("Множество a состоит из множества b")
# elif a >= b:
#     print("Множество b состоит из множества a")
# if a & b:
#     c = a & b
#     print(c)
# else:
#     print("Не пересекаются")

# Задание 4
# Создайте словарь из строки 'An apple a day keeps the doctor away'
# следующим образом: в качестве ключей возьмите символы строки, а
# значениями пусть будут числа, соответствующие количеству вхождений
# данной буквы в строку.
# a = 'An apple a day keeps the doctor away'
# b = {i: a.count(i) for i in a}
# print(b)

# Задание 5
# Ввести 10 чисел, данные числа добавить их во множество.
# a = 0
# b = set([])
# while a < 10:
#     c = int(input("Введите 10 чисел: "))
#     a += 1
#     b.add(c)
# print(b)

# Задание 6
# Выведите общее время звучания всех песен. Создайте список песен, время
# звучаниях которых больше 5 минут Создайте новый словарь тех песен, в
# название которых состоит из одного слова
# songs = { 'World in My Eyes': 4.76,
#           'Sweetest Perfection': 5.43,
#           'Personal Jesus': 4.56,
#           'Halo': 4.30,
#           'Waiting for the Night': 6.07,
#           'Enjoy the Silence': 4.6,
#           'Policy of Truth': 4.88,
#           'Blue Dress': 4.18,
#           'Clean': 5.68}
# long = 0
# for i in songs:
#     if songs[i] > 5:
#         spisok = list(songs.keys())
#         long += songs[i]
# print("Общее время звучания: ", long)
# print("Список песен, которые дольше 5 минут: ", spisok)
# new = {k: songs[k] for k in songs.keys() if not " " in k}
# print(new)

# Задание 7
# Дана строка. Сохранить в ней только первые вхождения символов,
# удалив все остальные. Результат вывести в виде кортежа.
# a = str(input("Введите строку: "))
# c = a.lower()
# b = c.split(" ")
# t = [i[:1] for i in b]
# print(tuple(t))

# Задание 8
# Сжать массив, удалив из него все элементы, величина которых
# находится в интервале [а, b]. Освободившиеся в конце массива элементы
# заполнить нулями.
# from random import *
# lists = []
# a = int(input('Нижняя граница массива: '))
# b = int(input('Верхняя граница массива: '))
# for i in range(10):
#     s = int(randint(a, b))
#     lists.append(s)
# print(lists, "\nУдалим элементы между a и b")
#
# c = int(input('Нижняя граница: '))
# d = int(input('Верхняя граница: '))
# i = 0
# m = 10
# while i < m:
#     if c <= lists[i] <= d:
#         del lists[i]
#         m -= 1
#     else:
#         i += 1
# for i in range(m, 10):
#     lists.append(0)
# print(lists)

# Задание 9
# from random import *
# N = int(input("Количество строк и столбцов: "))
# matrix = [[0] * N for i in range(N)]
# print(matrix, '\n')  # Создание списка с вложенным списком
#                      # со значениями 0
# otrelem = 0
# for i in range(N):
#     for j in range(N):
#         matrix[i][j] = randint(-10, 10)
#         print(matrix[i][j], end='\t')
#     print()
# # Создал матрицу 4*4 с рандомными значениями от -10 до 10
# for i in range(N):
#     for j in range(N):
#         if matrix[i][j] < 0 and j < i: # j < i под главной линией
#             otrelem += 1
# print(f'\nКоличество отрицательных элементов под главной '
#       f'диагональю: {otrelem}')

# Задание 10
# Найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный
# элементы в сумму не включать.

# Решение с помощью ввода
# from random import *
# lists = []
# a = int(input('Нижняя граница списка: '))
# b = int(input('Верхняя граница списка: '))
# for i in range(10):
#     s = int(randint(a, b))
#     lists.append(s)
#     lists.sort()
# print(f'\nОтсортированный список элементов: \n{lists}')
# print(f'\nСумма элементов между мин и макс значениями без этих элементов: '
#       f'{sum(lists[1:-1])}')

# Можно и проще делать ниже 2 способа создания списка =))
# import random
# a = [i for i in range(10)]
# b = [i for i in range(random.randint(1, 10), random.randint(10, 20))]
# a.sort()
# print(f'Список a {a}')
# b.sort()
# print(f'Список b {b}')
# print(f'Сумма между мин и макс в списке a: ', sum(a[1:-1]))
# print(f'Сумма между мин и макс в списке b: ', sum(b[1:-1]))
