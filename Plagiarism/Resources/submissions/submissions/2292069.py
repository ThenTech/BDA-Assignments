def fibonacci_values(i):
    lijst = []
    if i < 0:
        return None
    else:
        for getal in range(i-1):
            if getal == 0:
                lijst.append(getal)
                voriggetal = getal
            elif getal == 1:
                lijst.append(getal+voriggetal)
                tweeterug = voriggetal
                voriggetal = getal
            else:
                lijst.append(tweeterug + voriggetal)
                tweeterug = voriggetal
                voriggetal = getal
        return lijst
                