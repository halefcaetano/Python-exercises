from exe109 import modulo

price = float(input('Enter the price: '))
print(f'The half of {modulo.coin(price)} is {modulo.half(price, True)}.')
print(f'Double {modulo.coin(price)} is {modulo.double(price, True)}.')
print(f'Increasing 10% we have {modulo.increase(price, 10, True)}.')
print(f'Reducing 13% we have {modulo.take(price, 13, True)}.')