from time import sleep


def bigger(* num):
    print('Analyzing the values...')
    for i, c in enumerate(num):
        if i == 0:
            big = c
        else:
            if c > big:
                big = c
        print(c, end=' ')
        sleep(0.5)
    print(f' {len(num)} values were informed in total.')
    print(f'The highest value was {big}.')


bigger(10, 30, 40, 55, 1, 90, 3)
bigger(90, 20, 200)
bigger(4, 40, 5, 7, 9)
bigger(5, 8, 10, 30, 100, 9, 8)
