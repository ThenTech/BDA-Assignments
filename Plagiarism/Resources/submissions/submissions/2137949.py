jaar = int(input('Geef het jaartal:'))
if jaar % 400 == 0:
    print('Het is een schrikkeljaar.')
elif jaar % 100 == 0:
    print('Het is geen schrikkeljaar.')
else:
    if jaar % 4 == 0:
        print('Het is een schrikkeljaar.')
