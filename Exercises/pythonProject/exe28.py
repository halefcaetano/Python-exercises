from random import randint
n = randint(0, 5)
n1 = int(input('Guess the number: '))
if n == n1:
    print("The number is {} and you're right!" .format(n))
else:
    print("The number is {} and you're wrong!" .format(n))

