from datetime import date
s = 0
today = date.today().year
for c in range(0, 7):
    age = int(input('Enter year of birth: '))
    if (today - age) >= 21:
        s += 1
print('{} are of age.' .format(s))
print('{} are minors.' .format(7 - s))



