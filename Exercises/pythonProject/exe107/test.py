import modulo

price = float(input('Enter the price: '))
print(f'The half of {price} is {modulo.half(price)}.')
print(f'Double {price} is {modulo.double(price)}.')
print(f'Increasing 10% we have {modulo.increase(price)}.')
print(f'Reducing 13% we have {modulo.take(price)}.')