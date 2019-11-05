jaar = int(input('Geef het jaartal:'))
if jaar % 400 == 0:
    print(jaar,'is a leap year.')
elif jaar % 100 == 0:
    print(jaar, 'is not a leap year')
else:
    if jaar % 4 == 0:
        print(jaar,'is a leap year')
