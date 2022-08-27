odd = 0
for c in range(1, 500):
    if c % 3 == 0 and c % 2 != 0:
        odd += c
print('The sum of odd multiples of three between 1 and 500 is {}.' .format(odd))


