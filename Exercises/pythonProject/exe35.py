t = float(input('Enter the first measure: '))
t1 = float(input('Enter the second measure: '))
t2 = float(input('Enter the third measure: '))
if t + t1 > t2 and t + t2 > t1 and t1 + t2 > t:
    print('The measurements form a triangle.')
else:
    print('The measurements do not form a triangle.')
