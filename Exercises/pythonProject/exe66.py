n = count = s = 0
while True:
    n = int(input('Enter a number: '))
    if n == 999:
        break
    count += 1
    s += n
print(f'{count} numbers were entered and the sum of the numbers is {s}.')
