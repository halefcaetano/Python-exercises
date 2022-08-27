n1 = float(input('Enter the first value: '))
n2 = float(input('Enter the second value: '))
menu = 0
while menu != 5:
    menu = int(input('Type: \n[1] add\n[2] multiply\n[3] biggest\n{4] new numbers\n[5] exit program\n'))
    if menu == 1:
        print('The sum of the two numbers is {}.' .format(n1 + n2))
    elif menu == 2:
        print('The multiplication of the two numbers is {}.' .format(n1 * n2))
    elif menu == 3:
        if n1 > n2:
            print('The biggest number is {}.' .format(n1))
        elif n1 < n2:
            print('The biggest number is {}.' .format(n2))
        else:
            print('The numbers are the same.')
    elif menu == 4:
        n1 = float(input('Enter the first value: '))
        n2 = float(input('Enter the second value: '))
    else:
        print('The end.')
