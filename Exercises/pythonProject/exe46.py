from time import sleep
print('Countdown to fireworks.')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('Fireworks!')
