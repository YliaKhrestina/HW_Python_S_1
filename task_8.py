# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*
# 3 2 4 -> no
# 3 2 1 -> yes

n, m, k = map(int, input().split())

# Проверяем условие, что произведение n и m делится на k без остатка
if (n * m) % k == 0:
    print("yes")
else:
    print("no")