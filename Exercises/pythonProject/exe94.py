choice = 'S'
l = []
lw = []
l2 = []
woman = age = media = count = 0
while choice != 'N':
    data = {'Name': str(input('Enter the name: ')), 'Age': int(input('Enter the age: '))}
    while True:
        data['Gender'] = str(input('Enter the gender: M/F ')).upper()
        if data['Gender'] in 'MF':
            break
        print('Please enter M or F only.')
    l.append(data)
    for i in data.values():
        if i == 'F':
            lw.append(data['Name'])
        if type(i) == int:
            age += i
            count += 1
    media = age / count
    for c in data.values():
        if type(c) == int and c >= media:
            l2.append(data)
    while True:
        choice = str(input('Do you want to continue? Y/N ')).upper()
        if choice in 'YN':
            break
        print('Please enter only Y or N.')
print(f'The group has {len(l)} people.')
print(f'The mean age is {media:.2f} years.')
if len(lw) != 0:
    print(f'The registered women were {lw}.')
else:
    print('No women were registered.')
print('List of people who are above average: \n', l2)
