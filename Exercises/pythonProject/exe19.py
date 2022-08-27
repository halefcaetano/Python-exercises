from random import choice
s1 = input('Write firs student: ')
s2 = input('Write second student: ')
s3 = input('Write third student: ')
s4 = input('Write forth student: ')
lst = [s1, s2, s3, s4]
chosen = choice(lst)
print('The chosen one is {}.' .format(chosen))
