# Задача 30: Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
#  Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.





a1 = int(input('введите первый элемент арифметической прогрессии a1  = : '))
d = int(input('введите разность элементов арифметической прогрессии d  = : '))
n = int(input('введите количество элементов арифметической прогрессии n  = : '))
for i in range(n):
    print(a1 + i * d, end=' ')

