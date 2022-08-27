def half(x=0):
    return x / 2


def double(x=0):
    return x * 2


def increase(x=0, y=0):
    p = x + (x * y / 100)
    return p


def take(x=0, y=0):
    p = x - (x * y / 100)
    return p


def coin(x=0, y='R$'):
    return f'{y}{x:.2f}'.replace('.', ',')
