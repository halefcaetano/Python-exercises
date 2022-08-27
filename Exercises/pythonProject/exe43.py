w = float(input('Enter your weight (kg): '))
h = float(input('Enter your height (m): '))
imc = w / (h * h)
if imc < 18.5:
    print('You are underweight.')
elif imc < 25:
    print('You are at your ideal weight.')
elif imc < 30:
    print('You are overweight.')
elif imc < 40:
    print('You are obese.')
else:
    print('You are morbidly obese.')
