times = ('Palmeiras', 'Corinthians', 'Fluminense', 'Athletico-Pr', 'Flamengo', 'Internacional', 'Atletico-Mg',
         'Bragantino', 'Santos', 'Sao Paulo', 'Goias', 'Botafogo', 'America-Mg', 'Ceara', 'Coritiba', 'Avai',
         'Cuiaba', 'Fortaleza', 'Atletico-Go', 'Juventude')
print(f'The top five are: {times[0:5]}')
print(f'The last four in the table are: {times[16:20]}')
print(sorted(times))
print(f"Sao Paulo is in {times.index('Sao Paulo') + 1}h place")

