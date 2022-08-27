largest = 0
smallest = 0
for c in range(1, 6):
    w = float(input('Enter the weight of {} person: ' .format(c)))
    if c == 1:
        largest = w
        smallest = w
    else:
        if w > largest:
            largest = w
        if w < smallest:
            smallest = w
print('The largest weight is {} and the smallest weight is {}.' .format(largest, smallest))

