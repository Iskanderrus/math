import numpy as np

"""
Задача 1
векторы 
a = (3, 2.5, 7)
b = (8, 4, -6)
c = (1, -15, 5)
d = (12, 0, 4)

Определите координаты вектора e = 2(a + 2.5b) - c + d/4

"""

a = np.array([3, 2.5, 7])
b = np.array([8, 4, -6])
c = np.array([1, -15, 5])
d = np.array([12, 0, 4])

e = 2*(a + 2.5*b) - c + d/4
print(e)
