def readInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERROR. Please type a valid integer.')
            continue
        except KeyboardInterrupt:
            print('It was not typed a number')
            return 0
        else:
            return n


def readFloat(msg):
    while True:
        try:
            n2 = float(input(msg))
        except (ValueError, TypeError):
            print('ERROR. Please type a valid integer.')
            continue
        except KeyboardInterrupt:
            print('It was not typed a number')
            return 0
        else:
            return n2



r = readInt('Enter a number: ')
r2 = readFloat('Enter a real number: ')
print(f'You entered the number {r} and the number {r2}')