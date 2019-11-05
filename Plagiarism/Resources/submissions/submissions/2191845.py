def count_words(string):
    lengthe = len(string)
    seperators = " "
    for lengthe == 0:
        return 0
    teller =1
    for i in range(lengthe-1):
        if string[i] == seperators:
            teller+=1
        elif string[i] == ",":
            teller +=1
        elif string[i] == ".":
            teller +=1
    return teller
print(count_words("five 6 seven,eight!nine"))