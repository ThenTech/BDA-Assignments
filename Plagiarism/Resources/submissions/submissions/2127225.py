een = int(input('Hoeveel centjes van 1 eurocent heb je? '))
twee = int(input('Hoeveel centjes van 2 eurocent heb je? '))
vijf = int(input('Hoeveel centjes van 5 eurocent heb je? '))
tien = int(input('Hoeveel centjes van 10 eurocent heb je? '))
twintig = int(input('Hoeveel centjes van 20 eurocent heb je? '))
som = een*0.01 + twee*0.02 + vijf*0.05 + tien*0.10 + twintig*0.20
print('You have', som, 'euro!')