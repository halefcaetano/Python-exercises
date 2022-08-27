number = int(input('Write a number: '))
print('Enter 1 if you want to convert to binary. \nEnter 2 if you want to convert to octal. ''\nEnter 3 if you want '
      'to convert to hexadecimal.')
choice = int(input(''))
if choice == 1:
    print('The binary number of the number {} is {}.' .format(number, format(number, 'b')))
elif choice == 2:
    print('The octal number of the number {} is {}.' .format(number, format(number, 'o')))
elif choice == 3:
    print('The hexadecimal number of the number {} is {}.' .format(number, format(number, 'x')))
else:
    print('The options are from 1 to 3.')
