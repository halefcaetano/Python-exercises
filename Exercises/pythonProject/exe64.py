n = 0
count = 0
total = 0
while n != 999:
    n = float(input('Enter the number or enter 999 to stop: '))
    total += n
    count += 1
print('The sums of the numbers is {}.' .format(total - 999))
print('{} numbers were entered.' .format(count - 1))
