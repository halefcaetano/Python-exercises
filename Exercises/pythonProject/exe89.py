l = [[], [], [], [], []]
media = choice = count = 0
while choice != 'N':
    name = str(input('Write the name: '))
    grade1 = float(input('Write the first grade: '))
    grade2 = float(input('Write the second grade: '))
    l[0].append(count)
    l[1].append(name)
    l[2].append(grade1)
    l[3].append(grade2)
    media = (grade1 + grade2) / 2
    l[4].append(media)
    count += 1
    choice = str(input('Do you wish to continue: Y/N ')).upper()
print(f'{"N":<4}{"Name":<10}{"Media":>8}')
for i in range(0, count):
    print(f'{l[0][i]:<4}{l[1][i]:<10}{l[4][i]:>8.1f}')
while True:
    choice2 = int(input("Do you want to show which student's grade? (enter 999 to stop) "))
    if choice2 == 999:
        break
    print(l[1][choice2], l[2][choice2], l[3][choice2])

