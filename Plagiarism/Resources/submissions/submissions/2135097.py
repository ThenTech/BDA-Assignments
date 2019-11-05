jaartal = int(input('Geef je jaartal in: '))
if jaartal % 4 == 0 and jaartal % 100 == 0 and (jaartal % 100 == 0 and jaartal % 400 == 0):
    print(jaartal, 'is a leap year')
else:
    print(jaartal, 'is not a leap year')