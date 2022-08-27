def factorial(x, show=False):
    """
    :param x: The number to be calculated
    :param show: (Optional) Whether or not to show the calculation
    :return: The factorial value of a number
    """
    f = 1
    for c in range(x, 0, -1):
        f *= c
        if show:
            if c > 1:
                print(f'{c} x', end=' ')
            else:
                print(f'{c} =', end=' ')
    return f


print(factorial(5, show=True))
