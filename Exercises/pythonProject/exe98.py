from time import sleep


def counter(a, b, c):
    s = a
    if c == 0:
        c = 1
    if c < 0:
        c = c * (-1)
    if a < b:
        print(a, end=' ')
        sleep(0.5)
        while s < b:
            s += c
            if s <= b:
                print(s, end=' ')
                sleep(0.5)
    if a > b:
        print(a, end=' ')
        sleep(0.5)
        while s > b:
            s -= c
            if s >= b:
                print(s, end=' ')
                sleep(0.5)


print('Count from 1 to 10 from 1 in 1. ')
print(counter(1, 10, 1))
print('Count from 10 to 0 of 2 in 2. ')
print(counter(10, 0, 2))
print("Now it's your turn to customize the count.")
a = float(input('Start: '))
b = float(input('End: '))
c = float(input('Step: '))
print(counter(a, b, c))
