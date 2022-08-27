def read(msg):
    valid = False
    while not valid:
        money = str(input(msg)).replace(',', '.').strip()
        if money.isalpha() or money == '':
            print(f'{money} is an invalid price.')
        else:
            valid = True
            return float(money)