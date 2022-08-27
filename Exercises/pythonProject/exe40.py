s1 = float(input('Write the first score: '))
s2 = float(input('Write the second score: '))
f = (s1 + s2) / 2
if f >= 7:
    print('Your final grade is {} and you passed.' .format(f))
elif f >= 5:
    print('Your final grade is {} and you are on the mend.' .format(f))
else:
    print('Your final grade is {} and you fail.' . format(f))
