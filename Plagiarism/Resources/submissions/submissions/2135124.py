jaartal = int(input('Geef jaartal '))
if jaartal % 4 == 0:
    if (jaartal%100 == 0) and (jaartal%400 != 0):
        print(jaartal, 'is not a leap year')
    else:
        print(jaartal, 'is a leap year')
else:
    print(jaartal, "is not a leap year")