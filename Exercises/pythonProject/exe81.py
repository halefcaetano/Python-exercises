numbers = list()
while True:
    n = int(input('Write a number: '))
    numbers.append(n)
    choice = str(input('Do you wish to continue? Y/N')).upper()
    if choice == 'N':
        break
if 5 in numbers:
    print('The number five was typed.')
else:
    print('The number five was not typed.')
print(f'{len(numbers)} numbers were entered.')
numbers.sort(reverse=True)
print(f'Descending order of numbers is {numbers}')