n = int(input('Enter a number: '))
result = 1
count = 1
while count <= n:
    result *= count
    count += 1
print('The factorial of the number {} is {}.' .format(n, result))
