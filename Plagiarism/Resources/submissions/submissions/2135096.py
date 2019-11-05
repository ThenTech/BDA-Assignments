jaartal = int(input('Geef jaartal '))
if jaartal % 4 == 0:
    if (jaartal%400 == 0) and (jaartal%100 == 0):
        print(jaartal, 'is a leap year')
    else:
        print(jaartal, "is not a leap year")