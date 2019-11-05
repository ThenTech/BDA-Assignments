totaal = 0
def convert(number):
    global totaal
    lengte = len(number)
    if lengte > 1:
        value = convert(number[1:])
    value = int(number[0]) * (10**(lengte-1))
    totaal += value
    return totaal
    
convert("12345")
print(totaal)