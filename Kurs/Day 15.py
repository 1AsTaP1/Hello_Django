# Задача 1
# a = int(input("введите 1 число "))
# b = int(input("введите 2 число "))
# if a-b == 135:
#     print("Yes")
# elif b-a == 135:
#     print("Yes")
# else:
#     print("No")

# Задача 2
# from random import randint
# a = randint(-1000, 1000)
# print(a)
# if a > 100 or a < -100:
#     print("-")
# else:
#     print("+")

# Задача 3
# a = int(input("введите 1 число "))
# b = int(input("введите 2 число "))
# c = int(input("введите 3 число "))
# if a > 10 and b > 10 and c > 10:
#     print("Yes")
# else:
#     print("No")

# Задача 4
# a = 0
# while a <= 100:
#     a = int(input("Введите число "))
#     if a > 100:
#         break
#     elif a < 10:
#         continue
# print(a)

# Задача 5
# a = [i for i in range(-10, 11)]
# b = []
# for i in a:
#     if i % 2 == 0 and i > 0:
#         b.append(i)
# print(sum(b))

# Задача 6
# a = int(input("Введите 1 число: "))
# b = int(input("Введите 2 число: "))
# c = 0
# d = 0
# for i in range(a, b+1):
#     if i % 3 == 0:
#         c += i
#         d += 1
#     i += 1
# print(c / d)

# Задача 7
# a = int(input("Введите целое: "))
# b = 0
# while a != 0:
#     b = b + a % 10
#     a = a // 10
# print(b)

# Задача 8
# a = str(input("Введите строку: "))
# while True:
#     if len(a) >= 10:
#         print("!!!")
#         break
#     elif len(a) < 10:
#         print(a[1])
#         break

# Задача 9
# a = str(input("Введите строку: ")).split()
# c = []
# for i in a:
#     c.append(i + "!")
# print(c)

# Задача 10
# a = str(input("Введите строку: ")).split(',')
# c = []
# for i in a:
#     c.append(i + "_world")
# print(",\t".join(c))

# Задача 11
# from random import randint
# a = [randint(10, 100) for i in range(10)]
# b = []
# for i in a:
#     if i % 2 != 0:
#         b.append(i)
# print(b)

# Задача 12
# a = [i for i in range(50, 70+1) if i > 65]
# print(tuple(a))

