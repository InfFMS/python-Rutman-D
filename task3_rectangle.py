# Задача 3: Периметр и площадь прямоугольника
# Напишите программу, которая запрашивает у пользователя длину и ширину прямоугольника и выводит его периметр и площадь.
# Пример:
# Ввод: 4, 7
# Вывод: Периметр: 22, Площадь: 28
n = int(input())
m = int(input())
print("Периметр:", 2*(n+m))
print("Площадь:", n*m)