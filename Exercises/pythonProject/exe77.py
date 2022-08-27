list = ('python', 'halef', 'study', 'work', 'tomorrow', 'nobody', 'today', 'exercise', 'now', ' sleep', 'hungry')
for word in list:
        print(f'\nThe word {word} contains these vowels', end=' ')
        for letter in word:
                if letter in 'aeiou':
                        print(letter, end=' ')

