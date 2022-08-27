n1 = int(input('Write the first number: '))
n2 = int(input('Write the second number: '))
n3 = int(input('Write the third number: '))
if n1 > n2 and n1 > n3:
    print('The biggest number is ', n1)
if n2 > n1 and n2 > n3:
    print('The biggest number is ', n2)
if n3 > n1 and n3 > n2:
    print('The biggest number is ', n3)
if n1 < n2 and n1 < n3:
    print('The smallest is ', n1)
if n2 < n1 and n2 < n3:
    print('The smallest is ', n2)
if n3 < n1 and n3 < n2:
    print('The smallest is ', n3)
