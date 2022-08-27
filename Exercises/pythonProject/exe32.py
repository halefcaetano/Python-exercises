y = int(input('Write the year: '))
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print('The year {} is leap year.' .format(y))
else:
    print('The year {} is not a leap year.'.format(y))
