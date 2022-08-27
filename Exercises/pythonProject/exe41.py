from datetime import date
year = int(input('Enter the year of your birth: '))
today = date.today().year
age = today - year
if age <= 9:
    print('You are {} years old and your category is the little.' .format(age))
elif age <= 14:
    print('You are {} years old and your category is the infant.' .format(age))
elif age <= 19:
    print('You are {} years old and your category is the junior.' .format(age))
elif age <= 20:
    print('You are {} years old and your category is the senior.' .format(age))
else:
    print('You are {} years old and your category is the master.' .format(age))
