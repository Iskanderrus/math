import numpy as np

# Скалярное произведение векторов

print(3 * 8 * np.cos(np.pi/6))
print(12 * np.sqrt(3))
print()

print(6*4*np.cos(np.pi/4))
print(12 * np.sqrt(2))

print()
print(1.5*16*np.cos(2*np.pi/3))

print()
print(10*2.4*np.cos(np.pi/2))

# _________________________________
print('Second')
a = 5
b = 6
alpha = np.pi/4
beta = 2*np.pi/3

print(a**2)
print(b**2)
print(a*b*np.cos(2*alpha))
print(a*np.cos(alpha)*b)
print(a*b*np.cos(beta))
print(a*3*b*np.cos(beta))

# __________________________________
print('Third')
c = 11*np.sqrt(2)
d = 4
angle = np.pi/4

a = 5*c-d
b = 2*c+3*d

# a * b * cos(angle)
'''
(5c-d)*(2c+3d) = 10c**2 + 15c*d - d*2c - 3d**2

'''
print(round(10*c**2 + 13*d*c*np.cos(angle) - 3*d**2, 0))

# __________________________________________________
# Scalar multiplication - using coordinates
print('Fourth')
c = (4, 1, -5)
d = (2, -6, -3)

# a = 3*c + d = 3(4, 1, -5) + (2, -6, -3) = (12, 3, -15) + (2, -6, -3) = (14, -3, -18)
# b = -4*c + 6*d = -4(4, 1, -5) + 6(2, -6, -3) = (-16, -4, 20) + (12, -36, -18) = (-4, -40, 2)

scalar = (14*-4) + (-3*-40)+(-18*2)
print(scalar)


c = np.array(c)
d = np.array(d)

a = np.array(3 * c + d)
b = np.array(-4 * c + 6 * d)

scalar = a @ b
print(f'Last: {scalar}')
