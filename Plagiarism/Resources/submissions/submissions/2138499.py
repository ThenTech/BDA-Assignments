for el in alfabet:
    teller = 0
    for waarde in string_lijst:
        if el == waarde:
            teller =+ 1
    print(el, teller, sep=": ")