l = []
n1 = n2 = 0
for c in range(0, 9):
    l.append(int(input(f'Enter a value for [{n1}, {n2}] ')))
    n2 += 1
    if n2 > 2 and n1 == 0:
        n1 = 1
        n2 = 0
    if n2 > 2 and n1 == 1:
        n1 = 2
        n2 = 0
print(f'[   {l[0]}   ] [   {l[1]}   ] [   {l[2]}   ]\n[   {l[3]}   ] [   {l[4]}   ] [   {l[5]}   ]\n'
      f'[   {l[6]}   ] [   {l[7]}   ] [   {l[8]}   ]')
