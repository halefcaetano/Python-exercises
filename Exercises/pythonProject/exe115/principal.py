from exe115.lib.interface import *
from time import sleep
from exe115.lib.file import *

file = 'cursovideo.txt'

if not exist(file):
    create(file)

while True:
    r = menu(['See registered people', 'Register people', 'Log out of the system'])
    if r == 1:
        read(file)
    elif r == 2:
        title('New register')
        name = str(input('Enter the name: '))
        age = readInt('Enter the age: ')
        register(file, name, age)
    elif r == 3:
        print('Exiting the system.')
        break
    else:
        print('ERROR. Enter a valid number: ')
    sleep(1)
