team = []
player = {}
games = []
while True:
    player.clear()
    player['Name'] = str(input('Enter the name: '))
    total = int(input(f'How many games did {player["Name"]} play? '))
    games.clear()
    for c in range(0, total):
        games.append(int(input(f'How many goals during game {c + 1}? ')))
    player['Goals'] = games[:]
    player['Total'] = sum(games)
    team.append(player.copy())
    while True:
        answer = str(input('Do you wish to continue? Y/N ')).upper()[0]
        if answer in 'YN':
            break
        print('Answer only Y or N.')
    if answer == 'N':
        break
print('cod ', end='')
for i in player.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(team):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    find = int(input('Show data from which player? (999 o stop)'))
    if find == 999:
        break
    if find >= len(team):
        print('There is no player with this search code.')
    else:
        print(f'Player Lifting: {team[find]["Name"]}')
        for i, g in enumerate(team[find]['Goals']):
            print(f'In the game {i + 1} he made {g} goals.')