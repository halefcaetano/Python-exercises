numbers = list()
while True:
    n = int(input('write a numer: '))
    if n not in numbers:
        numbers.append(n)
    else:
        print('The number is already in list')
    choice = str(input('Do you wish to continue? Y/N')).upper()
    if choice == 'N':
        break
numbers.sort()
print(f'The added values were{numbers}')