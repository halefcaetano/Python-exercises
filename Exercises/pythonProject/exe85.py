l = [[], []]
for c in range(0, 7):
    n = int(input('Write a number: '))
    if n % 2 == 0:
        l[0].append(n)
    else:
        l[1].append(n)
l[0].sort()
l[1].sort()
print(f'The even values are {l[0]}.')
print(f'The odd values are {l[1]}.')
