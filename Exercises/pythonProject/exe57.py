sex = str(input('Enter gender [M/F]: '))
while sex != 'M' and sex != 'F':
    sex = str(input('Type capital M for male and capital F for female [M/F]: '))
print('The gender is {}.' .format(sex))
