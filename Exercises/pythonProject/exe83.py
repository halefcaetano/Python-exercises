phrase = str(input('Write the phrase: '))
p = list()
for s in phrase:
    if s == '(':
        p.append('(')
    elif s == ')':
        if len(p) > 0:
            p.pop()
        else:
            p.append(')')
            break
if len(p) == 0:
    print('ok')
else:
    print('not ok')
