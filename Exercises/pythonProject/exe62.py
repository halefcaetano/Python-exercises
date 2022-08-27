a = int(input('Enter the first term of an arithmetic progression: '))
r = int(input('Enter the ratio of an arithmetic progression: '))
count = 1
new = 10
total = 0
while new != 0:
    total += new
    while count <= total:
        print('{}' .format(a), end='')
        print(' - ' if count < total else '', end='')
        a += r
        count += 1
    new = int(input('\nHow many more terms do you want to show? '))

