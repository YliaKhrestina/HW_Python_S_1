# Задача 28: 
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 


def sum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a > b:
        return sum(a - 1, b + 1)
    else:
        return sum(a + 1, b - 1)

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

result = sum(A, B)
print(result)


