t = float(input('Enter the first measure: '))
t1 = float(input('Enter the second measure: '))
t2 = float(input('Enter the third measure: '))
if t + t1 > t2 and t + t2 > t1 and t1 + t2 > t:
    if t == t1 and t1 == t2:
        print('An equilateral triangle will be formed.')
    elif t == t1 or t1 == t2:
        print('An isosceles triangle will be formed.')
    else:
        print('A scalene triangle will be formed.')
else:
    print('The measurements do not form a triangle.')
