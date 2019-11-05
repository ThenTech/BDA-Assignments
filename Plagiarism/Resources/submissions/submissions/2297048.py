def lucky_numbers(n):
    lijst = []
    for i in range(1, n+1):
        lijst.append(i)
    tellerwhileloop = 2
    while tellerwhileloop <= len(lijst):
        zonder_elementen = lijst[:]
        tellerelementen = 0
        for i in zonder_elementen:
            if tellerelementen + 1 == tellerwhileloop:
                zonder_elementen.remove(i)
                tellerelementen = 1
            else:
                tellerelementen += 1
        tellerwhileloop += 1
        lijst = zonder_elementen
    return lijst