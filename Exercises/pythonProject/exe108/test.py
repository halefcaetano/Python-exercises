from exe108 import modulo

price = float(input('Enter the price: '))
print(f'The half of {modulo.coin(price)} is {modulo.coin(modulo.half(price))}.')
print(f'Double {modulo.coin(price)} is {modulo.coin(modulo.double(price))}.')
print(f'Increasing 10% we have {modulo.coin(modulo.increase(price))}.')
print(f'Reducing 13% we have {modulo.coin(modulo.take(price))}.')