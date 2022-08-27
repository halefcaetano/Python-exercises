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
