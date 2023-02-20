# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Введите n: '))
m = int(input('Введите m: '))
k = int(input('Введите k: '))


isPossible = False # объявляем флаг возможности решения

for i in range(1, m): 
    if (n * i == k):
        isPossible = True
        break
if (not isPossible):
    for i in range(1, n - 1): # m * n - уже проверяли в предыдущем цикле, поэтому n - 1
        if (m * i == k):
            isPossible = True
            break

print("можно" if isPossible else "нельзя")
