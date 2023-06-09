# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*
# 385916 -> yes
# 123456 -> no



ticket_number = input("Введите номер билета: ")

# Проверяем, что номер состоит из шести цифр
if len(ticket_number) != 6:
    print("Некорректный номер билета")
else:
# Разделяем номер на три первые и три последние цифры
    first_half = int(ticket_number[:3])
    second_half = int(ticket_number[3:])

# Сравниваем сумму первых трех цифр с суммой последних трех цифр
if sum(map(int, str(first_half))) == sum(map(int, str(second_half))):
    print("yes")
else:
    print("no")