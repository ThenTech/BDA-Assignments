def lucky_numbers(n):
    lijst = []
    lijst2 = []
    for i in range(n):
        lijst.append(i+1)
    print(lijst)
    element = 2
    while element <= len(lijst):
        for i in range(len(lijst)-1):
            if lijst[i] % element == 0:
                lijst2.append(lijst[i])
        for i in range(len(lijst)-len(lijst2)):
            if lijst[i] in lijst2:
                del lijst[i]
        lijst2 = []
        element += 1
                
    print(lijst)

lucky_numbers(22)