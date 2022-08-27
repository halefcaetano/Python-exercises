d = float(input('Enter the distance of your trip: '))
if d <= 200:
    print('The value of your ticket will be {} dollars.' .format(d * 0.50))
else:
    print('The value of your ticket will be {} dollars.'.format(d * 0.45))
