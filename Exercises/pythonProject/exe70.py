total = dollars100 = cheap = name = count = 0
while True:
    product = str(input('Enter the product name: '))
    price = float(input('Enter product price: '))
    total += price
    count += 1
    if price > 100:
        dollars100 += 1
    if count == 1:
        name = product
        cheap = price
    else:
        if price < cheap:
            cheap = price
            name = product
    choice = ' '
    while choice not in 'YN':
        choice = str(input('Want to add more product? [Y/N] ')) .upper()[0]
    if choice == 'N':
        break
print(f'The total spend is {total} dollars. {dollars100} products cost over 100 dollars. The cheapest product is '
      f'{name}.')
