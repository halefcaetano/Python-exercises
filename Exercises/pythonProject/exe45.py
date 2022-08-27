from random import randint
player = str(input("Let's Play! Do you choose rock, paper or scissors? ")) .lower() .strip()
machine = randint(1, 3)
# 1 = 'scissors' // 2 = 'paper' // 3 = 'rock'
if player == 'scissors':
    if machine == 1:
        print('I also chose scissors, so we tied.')
    elif machine == 2:
        print('I chose paper. You are the winner.')
    else:
        print('I chose rock. I won.')
elif player == 'rock':
    if machine == 3:
        print('I also chose rock, so we tied.')
    elif machine == 2:
        print('I chose paper. I won.')
    else:
        print('I chose scissors. You are the winner.')
else:
    if machine == 3:
        print('I chose rock. You are the winner.')
    elif machine == 2:
        print('I also chose paper, so we tied.')
    else:
        print('I chose scissors. I won.')
