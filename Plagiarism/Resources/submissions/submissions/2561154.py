def lucky_numbers(n):
    lijst = []
    lijst2 = []
    for i in range(n):
        lijst.append(i+1)
    element = 2
    while element <= len(lijst):
        for i in range(len(lijst)):
            if (i+1) % element == 0:
                lijst2.append(lijst[i])
        for i in range((len(lijst)-len(lijst2))):
            if lijst[i] in lijst2:
                del lijst[i]
        if element % 2 == 0:
            del lijst[len(lijst)-1]
        lijst2 = []
        element += 1
    return lijst

print(lucky_numbers(22))