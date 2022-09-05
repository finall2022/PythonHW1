""" 5 Напишите программу, которая принимает на вход координаты 
двух точек и находит расстояние между ними в 2D пространстве.

*Пример:*

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
 """
import math
print('Введите координаты x,y точки A')
xa = float(input())
ya = float(input())
print('Введите координаты x,y точки B')
xb = float(input())
yb = float(input())
AB = (xb-xa)*(xb-xa)+(yb-ya)*(yb-ya)
sqrt = math.sqrt(AB)
print('Расстояние между точками равно ' + str(round(sqrt,2)))
