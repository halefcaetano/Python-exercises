adult = man = woman20 = 0
while True:
    age = int(input('Enter age: '))
    gender = ' '
    while gender not in 'MF':
        gender = str(input('Enter gender: [M/F] ')) .upper()[0]
    if age > 18:
        adult += 1
    if gender == 'M':
        man += 1
    if gender == 'F' and age < 20:
        woman20 += 1
    people = ' '
    while people not in 'YN':
        people = str(input('Want to add more people? [Y/N] ')).upper()[0]
    if people == 'N':
        break
print(f'{adult} over 18 years old. {man} men registered. {woman20} women under the age of 20 registered.')
