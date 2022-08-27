from random import randint
n = randint(0, 10)
n1 = int(input('Guess the number: '))
guesses = 1
while n != n1:
    n1 = int(input('Try again: '))
    guesses += 1
print("You're right, the number chosen was {}. You got the number right after {} attempts." .format(n, guesses))
