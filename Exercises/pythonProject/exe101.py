def vote(x):
    from datetime import date
    year = date.today().year
    a = year - x
    if (a > 18) and (a < 65):
        return f'At the age of {a} voting is mandatory.'
    elif a < 18:
        return f'At the age of {a} you will not be able to vote.'
    else:
        return f'At the age of {a} the vote is optional.'


age = int(input('Enter the year you were born: '))
print(vote(age))
