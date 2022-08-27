l = []
l2 = []
n1 = n2 = even = bigger = 0
for c in range(0, 9):
    l.append(int(input(f'Enter a value for [{n1}, {n2}] ')))
    n2 += 1
    if n2 > 2 and n1 == 0:
        n1 = 1
        n2 = 0
    if n2 > 2 and n1 == 1:
        n1 = 2
        n2 = 0
for b in l:
    if b % 2 == 0:
        even += b
bigger = l[3]
if l[3] < l[4]:
    bigger = l[4]
if l[4] < l[5]:
    bigger = l[5]
sum = l[2] + l[5] + l[8]
print(f'[   {l[0]}   ] [   {l[1]}   ] [   {l[2]}   ]\n[   {l[3]}   ] [   {l[4]}   ] [   {l[5]}   ]\n'
      f'[   {l[6]}   ] [   {l[7]}   ] [   {l[8]}   ]')
print(f'The sum of even values is {even}.')
print(f'The largest value of the second line is {bigger}.')
print(f'The sum of the third column is {sum}.')
