x = input('\033[4;34;40mWrite something: \033[m')
print("Class - {}" .format(type(x)))
print('Only have space?', x.isspace())
print('Is a number?', x.isnumeric())
print('Is alphabetic?', x.isalpha())




