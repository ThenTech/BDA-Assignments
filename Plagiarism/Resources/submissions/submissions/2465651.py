def convert(number):
    if len(number)==0:
        print(totaal)
    else:
        totaal += (int(number[0])*(10**lengte))
        number = number[1:]
        lengte = len(number)
        convert(number)
lengte = len(number)
totaal = 0