answer = ''
media = 0
count = 0
biggest = 0
smallest = 0
while answer != 'N':
    number = float(input('Enter a number: '))
    answer = str(input('Do you want to continue [Y/N]? ')) .upper()
    media += number
    count += 1
    if count == 1:
        smallest = number
        biggest = number
    else:
        if number < smallest:
            smallest = number
        if biggest < number:
            biggest = number
print('The smallest number is {}.' .format(smallest))
print('The average of the numbers is {:.2f}.' .format(media/count))
print('The biggest number is {}.' .format(biggest))
