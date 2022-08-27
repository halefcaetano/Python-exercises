a = int(input('Enter the first term of an arithmetic progression: '))
r = int(input('Enter the ratio of an arithmetic progression: '))
count = 1
while count <= 10:
    print('{}' .format(a), end='')
    print(' - ' if count < 10 else '', end='')
    a += r
    count += 1
