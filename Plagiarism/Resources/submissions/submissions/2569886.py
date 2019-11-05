def convert(number):
    som = 0
    if len(number) > 1:
        som = convert(number[1:])
    getal = int(number[0])*10**(len(number)-1)
    som = som + getal
    return som

