from random import randint
from time import sleep


def draw(num):
    print('Sorting the values:', end=' ')
    for i in range(0, 5):
        n = randint(0, 10)
        num.append(n)
        print(n, end=' ')
        sleep(0.5)
    print()


def even(num):
    s = 0
    for i in num:
        if i % 2 == 0:  
            s += i
    print(f'Adding the even values of {num}, we get {s}.')


numbers = list()
draw(numbers)
even(numbers)

