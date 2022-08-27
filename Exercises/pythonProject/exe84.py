heavier = lighter = 0
principal = []
while True:
    people = [str(input('Write the name: ')), float(input('Write the weight: '))]
    if len(principal) == 0:
        heavier = lighter = people[1]
    else:
        if people[1] > heavier:
            heavier = people[1]
        if people[1] < lighter:
            lighter = people[1]
    principal.append(people[:])
    people.clear()
    choice = str(input('Do you wish to continue? Y/N ')).upper()
    if choice == 'N':
        break
print(f'The total number of people registered was {len(principal)}.')
print(f'The biggest weights were {heavier}', end=' ')
for p in principal:
    if p[1] == heavier:
        print(f'The weight of {p[0]}', end=' ')
print()
print(f'The lightest weights were {lighter}', end=' ')
for p in principal:
    if p[1] == lighter:
        print(f'The weight of {p[0]}', end=' ')
