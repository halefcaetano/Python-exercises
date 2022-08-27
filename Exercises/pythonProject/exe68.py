from random import randint
count = 0
while True:
    n = int(input('Enter a number: '))
    c = str(input('Do you want even or odd? [E/O] ')) .upper()
    m = randint(1, 10)
    total = n + m
    if total % 2 == 0 and c == 'E':
        print(f'The computer chose {m}, the sum was {total} and you won because the total is even.')
        count += 1
    elif total % 2 != 0 and c == 'O':
        print(f'The computer chose {m}, the sum was {total} and you won because the total is odd.')
        count += 1
    else:
        print(f"The computer chose {m}, the sum was {total}. You've won {count} times. Lost now.")
        break





