n1 = int(input('Write the first number: '))
n2 = int(input('Write the first number: '))
if n1 > n2:
    print('The first number {} is bigger than second number {}.' .format(n1, n2))
elif n2 > n1:
    print('The second number {} i bigger than first number {}.' .format(n2, n1))
else:
    print('The numbers are the same.')
