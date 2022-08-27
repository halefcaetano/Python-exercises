n = int(input('Write a number: '))
mult = 0
for c in range(2, n):
    if n % c == 0:
        mult += 1
if mult == 0:
    print("It's a prime number")
else:
    print('Not a prime number')
