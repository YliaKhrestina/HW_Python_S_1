# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

N = int(input())  # Вводим количество элементов в массиве
A = list(map(int, input().split()))  # Вводим элементы массива
X = int(input())  # Вводим число X

closest = min(A, key=lambda num: abs(num - X))  # Находим ближайший элемент к числу X в массиве A

print(closest)  # Выводим результат