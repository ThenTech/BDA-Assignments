def count_words(string):
    lengthe = len(string)
    seperators = " "
    teller =0
    woorden = string.split()
    teller = len(woorden)
    for i in range(len(woorden)-1):
        for j in "0123456789":
            if i == j:
                teller-=1
    for i in range(len(woorden)):
        lengthe_2 = len(str(i))
        for j in ",?;.:/!0123456789":
            for k in range(lengthe_2-1):
                if j == k:
                    teller +=1
    if lengthe > 0:
        teller += 1
    return teller
print(count_words("five 6 seven,eight!nine"))