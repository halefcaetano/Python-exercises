l = 'Pyhelp help system'
manual = 'Accessing the manual'
end = 'See you later'
while True:
    print(f'\033[44m{"-" * len(l)}\33[m')
    print(f'\033[44m{l}\33[m')
    print(f'\033[44m{"-" * len(l)}\33[m')
    ask = str(input('Enter a function or library (Type end to end): '))
    if ask == 'end':
        break
    print(f'\033[41m{"-" * (len(manual) + len(ask) + 1)}\33[m')
    print(f'\033[41m{manual} {ask}\33[m')
    print(f'\033[41m{"-" * (len(manual) + len(ask) + 1)}\33[m')
    help(ask)
print(f'\033[46m{"-" * len(end)}\33[m')
print(f'\033[46m{end}\33[m')
print(f'\033[46m{"-" * len(end)}\33[m')
