p = float(input('Enter product price: '))
pm = float(input('What is the payment method: \n1- Payment in cash or check. \n2- Payment by card. \n3- Installed in 2 '
                 'installments on the card. \n4- Installed in 3 or more installments on the card. \n '))
if pm == 1:
    print('The final value of the product will be {} dollars.' .format(p - (p * 10 / 100)))
elif pm == 2:
    print('The final value of the product will be {} dollars.' .format(p - (p * 5 / 100)))
elif pm == 3:
    print('The final value of the product will be {} dollars.' .format(p))
elif pm == 4:
    print('The final value of the product will be {} dollars.' .format(p + (p * 20 / 100)))
else:
    print('Invalid option, try again.')
