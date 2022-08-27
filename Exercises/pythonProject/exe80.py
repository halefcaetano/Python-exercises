numbers = list()
for c in range(0, 5):
    n = int(input('Write a number: '))
    if c == 0:
        numbers.append(n)
    elif n > numbers[-1]:
        numbers.append(n)
    else:
        p = 0
        while p < len(numbers):
            if n <= numbers[p]:
                numbers.insert(p, n)
                break
            p += 1
print(numbers)

