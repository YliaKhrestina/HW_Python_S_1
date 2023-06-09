# Задача 32: 
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)


# Функция для определения индексов элементов в заданном диапазоне
def find_indexes(arr, min_value, max_value):
    indexes = []
    for i in range(len(arr)):
        if min_value <= arr[i] <= max_value:
            indexes.append(i)
    return indexes

# Пример использования
arr = [2, 4, 6, 8, 10, 12, 14]
min_value = 5
max_value = 11

result = find_indexes(arr, min_value, max_value)
print("Индексы элементов в заданном диапазоне:")
print(result)

