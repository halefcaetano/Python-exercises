numbers = list()
odd = list()
even = list()
while True:
    n = int(input('Write a number: '))
    numbers.append(n)
    choice = str(input('Do you wish to continue? Y/N')).upper()
    if choice == 'N':
        break
for c in numbers:
    if c % 2 == 0:
        even.append(c)
    else:
        odd.append(c)
print(f'The even numbers are {even}.')
print(f'The odd numbers are {odd}.')
print(f'The list with all the numbers is {numbers}.')
