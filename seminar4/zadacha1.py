# Задача 1
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
#  m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

list_1 = []
for i in range(int(input('введите количество элементов массива N = : '))):
    list_1.append(int(input('введите элемент массива = : ')))
print(list_1)


list_2 = []
for i in range(int(input('введите количество элементов массива M = : '))):
    list_2.append(int(input('введите элемент массива = : ')))
print(list_2)

# print(sorted(list_1))
# print(sorted(list_2))
# print((set(list_1)), (set(list_2)))

# print(max(list_1))
# print(min(list_1))

# не хватает знаний чтобы сделать это задание



