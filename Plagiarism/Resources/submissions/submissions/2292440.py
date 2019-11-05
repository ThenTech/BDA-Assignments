def fibonacci_values(i):
    lijst = []

    eenterug = 1
    tweeterug = 0
    if i < 0:
        return None
    else:
        for x in range(i):
            if x == 0:
                toevoegen = 0
                lijst.append(toevoegen)
            elif x == 1:
                toevoegen = 1
                lijst.append(toevoegen)
            else:
                toevoegen = eenterug + tweeterug
                lijst.append(toevoegen)
                tweeterug = eenterug
                eenterug = toevoegen


        return lijst

print(fibonacci_values(7))