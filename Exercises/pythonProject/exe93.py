goals = list()
total = 0
name = str(input('Enter the name: '))
games = int(input('How many games did he play? '))
for i in range(0, games):
    goalsGames = int(input(f'How many goals in the match {i + 1}? '))
    goals.append(goalsGames)
    total += goalsGames
geral = {'Name': name, 'Goals': goals, 'Total': total}
print(geral)
for v, k in geral.items():
    print(f'{v} has value {k}')
for c, p in enumerate(goals):
    print(f'In the match {c + 1}, {name} scored {p} goals.')