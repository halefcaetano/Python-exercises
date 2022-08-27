def readInt(msg):
    ok = False
    number = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            number = int(n)
            ok = True
        else:
            print('Enter a valid integer.')
        if ok:
            break
    return number


n = readInt('Enter a number: ')
print(f'You entered the number {n}.')