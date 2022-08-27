from math import pow, sqrt
a = float(input('Enter the adjacent side: '))
o = float(input('Enter the opposite side: '))
h = pow(o, 2) + pow(a, 2)
h1 = sqrt(h)
print('The length of the hypotenuse is {:.2f}.' .format(h1))





