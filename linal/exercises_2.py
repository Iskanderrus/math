import numpy as np

'''
для угла x, выраженного в радианах: 

np.sin(x) - синус угла x
np.cos(x) - косинус угла x
np.tan(x) - тангенс угла x
np.arcsin(x) - арксинус x
pn.arccos(x) - арккосину x

np.rad2deg(x) - перевод из радиан в градусы
np.deg2rad(x) - перевод из градусов в радианы 
np.pi/x - тоже перевод из градусов в радианы


'''

'''В треугольнике KLM угол M прямой, KM = 12, cos K = 0.8. 
Найдите KL

'''
km = 12
cos_k = 0.8
kl = km/0.8

print(kl)

'''
В треугольнике RTS угол S прямой, RT = 32, cos T = 0.5
Найдите TS.
'''
rt = 32
cos_t = 0.5
ts = rt * cos_t
print(ts)

# ____________________________________

print(np.rad2deg(3*np.pi/2))
print(np.rad2deg(35*np.pi/36))
print(np.rad2deg(19*np.pi/60))
print(np.rad2deg(11*np.pi/90))
print(np.rad2deg(77*np.pi/45))

# ____________________________________

print(np.sqrt(3) / 2)
print(np.sin(19*np.pi/3))
print()
print(np.sqrt(2) / 2)
print(np.cos(-15*np.pi/4))
print()
print(1 / np.sqrt(3))
print(np.tan(-11*np.pi/6))
print()
print(np.sqrt(3))

print(np.cos(36*np.pi/3))
print(np.tan(9*np.pi/4))

# EQUATIONS

print(round(np.arccos(1/2), 6) == round(np.pi/3, 6))
print(round(np.arcsin(-1/2), 6) == round(-1*np.pi/6, 6))
print(np.arccos(-1/2) == -2*np.pi/3)
print(np.arcsin(np.sqrt(3)/2) == 2*np.pi/3)
print(np.arccos(-1*np.sqrt(3)/2) == 5*np.pi/6)
print(np.arcsin(-1*np.sqrt(2)/2) == -1*np.pi/2)
print(np.arccos(np.sqrt(2)/2) == np.pi/4)