# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
#  Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
#   В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 3
# -> 1

list_1 = []
for i in range(int(input('введите количество элементов массива N = : '))):
    list_1.append(int(input('введите элемент массива = : ')))
print(list_1)
# list_1 = [1, 2, 3, 4, 5, 4, 6, 3]
x = int(input('введите число X = : '))
count = 0
for i in range(len(list_1)):
    if x == list_1[i]:
        count += 1
print(f'задуманное число X встречается - {count} раз')



