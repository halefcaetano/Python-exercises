def half(x=0, form=False):
    p = x / 2
    return p if form is False else coin(p)


def double(x=0, form=False):
    p = x * 2
    return p if form is False else coin(p)


def increase(x=0, y=0, form=False):
    p = x + (x * y / 100)
    return p if form is False else coin(p)


def take(x=0, y=0, form=False):
    p = x - (x * y / 100)
    return p if form is False else coin(p)


def coin(x=0, y='R$'):
    return f'{y}{x:.2f}'.replace('.', ',')


def resume(x=0, y=10, h=5):
    print('-' * 36)
    print('Summary of value'.center(36))
    print('-' * 36)
    print(f'Price:                  \t{coin(x)}')
    print(f'Double of the price:     \t{double(x, True)}')
    print(f'Half of the price:       \t{half(x, True)}')
    print(f'Price with {y} increase: \t{increase(x, y, True)}')
    print(f'Price taking away {h}:     \t{take(x, h, True)}')
    print('-' * 36)
