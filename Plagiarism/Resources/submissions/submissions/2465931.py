def convert(number):
    totaal = 0
    convert2(number,totaal)
def convert2(number,totaal):
    lengte = len(number)
    if len(number)==0:
        print(totaal)
    else:
        totaal += (int(number[0])*(10**lengte))
        number = number[1:]
        lengte = len(number)
        convert(number)
