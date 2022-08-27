house = float(input('Enter the house value: '))
salary = float(input('Enter your salary: '))
years = float(input('Enter the amount of years you want to pay: '))
monthly = house / (years * 12)
if monthly <= 30 * salary / 100:
    print('You will buy this house with monthly values of {:.2f} dollars.' .format(monthly))
else:
    print("You don't earn enough to buy this house.")
