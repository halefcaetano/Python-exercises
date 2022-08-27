s = float(input('Write tour salary: '))
if s > 1250:
    print('Your new salary will be {} dollars' .format(10 * s / 100 + s))
else:
    print('Your new salary will be {} dollars'.format(15 * s / 100 + s))

