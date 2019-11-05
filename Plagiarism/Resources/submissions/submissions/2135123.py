jaartal = int(input('Geef je jaartal in: '))
x = jaartal/400
if jaartal % 4 == 0 or (x % 4 == 0):
    print(jaartal, 'is a leap year')
else:
    print(jaartal, 'is not a leap year')