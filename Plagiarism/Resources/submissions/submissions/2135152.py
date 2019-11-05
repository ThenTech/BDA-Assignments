jaartal = int(input('Geef je jaartal in: '))
x = jaartal % 400
if jaartal % 4 == 0:
    if jaartal % 100 == 0 and x != 0:
        print(jaartal, 'is not a leap year')
    else:
        print(jaartal, 'is a leap year')
else:
    print(jaartal, 'is not a leap year')