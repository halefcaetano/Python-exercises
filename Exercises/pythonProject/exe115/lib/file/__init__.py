from exe115.lib.interface import *

def exist(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def create(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('ERROR')
    else:
        print(f'File {name} created')


def read(name):
    try:
        a = open(name, 'rt')
    except:
        print('ERROR')
    else:
        title('REGISTERED PERSONS')
        for l in a:
            d = l.split(':')
            d[1] = d[1].replace('\n', '')
            print(f'{d[0]:<30}{d[1]:>3} years old')
    finally:
        a.close()


def register(file, name='Unknown', age=0):
    try:
        a = open(file, 'at')
    except:
        print('ERROR')
    else:
        try:
            a.write(f'{name}:{age}\n')
        except:
            print('ERROR')
        else:
            print(f'{name} added')
        finally:
            a.close()
