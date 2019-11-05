dayb = input("what's your day of birth? ")
monthb = input("In what month were you born? ")
yearb = input("In what year were you born? ")
dayn = input("what is todays date? ")
monthn = input("what month are we? ")
yearn = input("In which year do we live? ")
x = 0
if monthb == 2 or monthn == 2:
    if yearb % 4 == 0:
        if yearb % 100 == 0:
            if yearb % 400 == 0:
                yearb = "leap year"
            else:
                yearb = "not a leap year"
        else:
            yearb = "leap year"
    else:
        yearb = "not a leap year"
    if yearn % 4 == 0:
        if yearn % 100 == 0:
            if yearn % 400 == 0:
                yearn = "leap year"
            else:
                yearn = "not a leap year"
        else:
            yearn = "leap year"
    else:
        yearn = "not a leap year"
else:
    x = x
if yearb == "leap year" or yearn == "leap year":
    if monthb == 2 or monthn == 2:
        if dayn == 29 or dayb == 29:
            x = x+1
yearn=int(yearn)
yearb=int(yearb)
x = x + (yearn - yearb)
print(x)