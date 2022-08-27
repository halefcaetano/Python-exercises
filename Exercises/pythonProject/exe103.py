def form(n, x):
    if n == '':
        n = 'unknown'
    if x == '':
        x = 0
    print(f'The player {n} scored {x} goals in the championship.')


name = str(input('Enter the name of the player: '))
score = str(input('How many goals did he score: '))
if score.isnumeric():
    score = int(score)
else:
    score = 0
form(name, score)
