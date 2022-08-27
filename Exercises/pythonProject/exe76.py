list = ('milk', 2, 'bread', 4.50, 'juice', 8, 'cake', 10, 'soda', 9.50, 'water', 3, 'cheese', 20)
for p in range(0, len(list)):
    if p % 2 == 0:
        print(f'{list[p]:.<30}', end='')
    else:
        print(f'{list[p]:>6.2f}')

