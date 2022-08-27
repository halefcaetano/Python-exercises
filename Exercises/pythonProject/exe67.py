while True:
    x = int(input('Enter a number: '))
    if x < 0:
        break
    for c in range(1, 11):
        print('{} x {} = {}'.format(x, c, x * c))
print('The end.')