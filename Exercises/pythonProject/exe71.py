n = int(input('Enter the amount: '))
total = n
banknotes = 50
totalBanknotes = 0
while True:
    if total >= banknotes:
        total -= banknotes
        totalBanknotes += 1
    else:
        if totalBanknotes > 0:
            print(f'Total of {totalBanknotes} banknotes of {banknotes}.')
        if banknotes == 50:
            banknotes = 20
        elif banknotes == 20:
            banknotes = 10
        elif banknotes == 10:
            banknotes = 1
        totalBanknotes = 0
        if total == 0:
            break
