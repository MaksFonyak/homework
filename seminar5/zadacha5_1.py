# Задача 1
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8



def expon_num(A,B):
    if B==1:
        return A
    if B!=1:
        return (A * expon_num(A, B - 1))

A = int(input('введите число A = : '))
B = int(input('введите число B = : '))
# print(expon_num(A, B))
print(f'{A} в степени {B} равно {expon_num(A, B)} ')




