numbers = list()
bigger = 0
smaller = 0
for c in range(0, 5):
    numbers.append(int(input('Write a number: ')))
    if c == 0:
        bigger = smaller = numbers[c]
    else:
        if numbers[c] > bigger:
            bigger = numbers[c]
        if numbers[c] < smaller:
            smaller = numbers[c]
print(f'The largest number was {bigger}.', end='')
for i, c in enumerate(numbers):
    if c == bigger:
        print(f' In position {i}.', end='')
print()
print(f'The smallest number was {smaller}.', end='')
for i, c in enumerate(numbers):
    if c == smaller:
        print(f' In position {i}.', end='')

