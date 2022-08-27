a = int(input('Enter the first term of an arithmetic progression: '))
r = int(input('Enter the ratio of an arithmetic progression: '))
n = 10
last = a + (n - 1) * r
print('The first ten terms of this arithmetic progression are: ')
for c in range(a, last + 1, r):
    print(c)