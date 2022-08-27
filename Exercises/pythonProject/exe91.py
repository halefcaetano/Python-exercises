from random import randint
count = 1
for c in range(0, 4):
    players = {'Player 1': randint(1, 6), 'Player 2': randint(1, 6), 'Player 3': randint(1, 6),
               'Player 4': randint(1, 6)}
for k, v in players.items():
    print(f'{k} made {v}')
for i in sorted(players, key=players.get, reverse=True):
    print(f'{count}° position: {i} with {players[i]}')
    count += 1
