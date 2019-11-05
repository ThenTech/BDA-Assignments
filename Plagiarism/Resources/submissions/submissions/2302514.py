def lijstmaken(n):
    lijst = []
    teller = 0
    for x in range((n)):
        teller += 1
        lijst.append(teller)
    return lijst
def lucky_numbers(n):
    lijst = lijstmaken(n)
    teller = 2
    teller2 = 1
    index = 0
    lijst2 = lijst[:]
    while teller <= len(lijst):
        lijst2 = lijst[:]
        for element in lijst:
            if teller == teller2:
                del lijst2[index]
                teller2 = 1
            else:
                teller2 += 1
                index += 1

        lijst = lijst2
        teller += 1
        index = 0
        teller2 = 1
    return lijst2

lucky_numbers(15)