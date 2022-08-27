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


def line(t=42):
    return '-' * 42


def title(msg):
    print(line())
    print(msg.center(42))
    print(line())


def menu(lst):
    title('Principal')
    c = 1
    for item in lst:
        print(f'{c} - {item}')
        c += 1
    print(line())
    choice = readInt('Enter a number:')
    return choice