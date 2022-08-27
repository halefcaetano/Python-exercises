p = input('Write a phrase: ') .strip() .lower()
print('The letter a appears {} times.' .format(p.count('a')))
print('The first time the letter a appears is in the {} position.' .format(p.find('a')+1))
print('The last time the letter a appears is in the {} position.' .format(p.rfind('a')+1))


