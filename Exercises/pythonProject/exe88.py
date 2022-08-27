from random import randint
from time import sleep
l = []
p = []
total = 1
games = int(input('How many games do you want: '))
while total <= games:
    count = 0
    while True:
        n = randint(1, 60)
        if n not in l:
            l.append(n)
            count += 1
        if count >= 6:
            break
    l.sort()
    p.append(l[:])
    l.clear()
    total += 1
for i, o in enumerate(p):
    print(f'Game {i + 1}: {o}')
