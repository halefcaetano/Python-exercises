from random import shuffle
s1 = input('Write firs student: ')
s2 = input('Write second student: ')
s3 = input('Write third student: ')
s4 = input('Write forth student: ')
lst = [s1, s2, s3, s4]
shuffle(lst)
print('The new order will be: {}.' .format(lst))

