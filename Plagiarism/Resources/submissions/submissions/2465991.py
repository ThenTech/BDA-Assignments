def convert(number):
    totaal = 0
    return convert2(number,totaal)
def convert2(number,totaal):
    lengte = len(number)
    if len(number)==0:
        return (totaal)
    else:
        totaal += (int(number[0])*(10**lengte-1))
        number = number[1:]
        lengte = len(number)
        return convert2(number,totaal)
