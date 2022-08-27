even = 0
for c in range(0, 6):
    c = int(input('Write a number: '))
    if c % 2 == 0:
        even += c
print('The sum of the even numbers is {}. ' .format(even))
