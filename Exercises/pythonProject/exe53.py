phrase = str(input('Write a phrase: ')) .strip() .lower()
p = phrase.replace(' ', '')
if p == p[::-1]:
    print("It's a palindrome phrase.")
else:
    print('It is not a palindrome phrase.')
