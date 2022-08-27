from datetime import date
year = int(input('Enter the year of your birth: '))
today = date.today().year
age = today - year
if age > 18:
    print('You passed the enlistment time, you should have enlisted {} years ago.' .format(age - 18))
elif age < 18:
    print("It's not time to enlist yet, you should enlist in {} years." .format(18 - age))
else:
    print('You should enlist this year.')

