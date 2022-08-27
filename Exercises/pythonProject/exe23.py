n = int(input('Write a number: '))
n1 = n // 1000 % 10
n2 = n // 100 % 10
n3 = n // 10 % 10
n4 = n // 1 % 10
print('Unit = ', n4)
print('Ten = ', n3)
print('Hundred = ', n2)
print('Thousand = ', n1)

