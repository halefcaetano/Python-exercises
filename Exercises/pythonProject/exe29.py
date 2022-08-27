s = int(input('Write your speed: '))
if s > 80:
    print('You got a ticket in the amount of {} dollars.' .format((s - 80) * 7))
