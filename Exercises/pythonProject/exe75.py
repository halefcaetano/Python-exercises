n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
n3 = int(input('Enter the third number: '))
n4 = int(input('Enter the forth number: '))
t = (n1, n2, n3, n4)
print(f'The number nine appears {t.count(9)} times.')
if 3 in t:
    print(f'The number three was first typed in the {t.index(3) + 1}th position.')
print('The even numbers are: ', end='')
for number in t:
    if number % 2 == 0:
        print(f' {number}', end='')


