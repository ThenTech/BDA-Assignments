def count_words(string):
    overbodig = "0123456789"
    string_new:""
    for i in range(len(string)-1):
        if string[i] not in overbodig:
            string_new += string[i]
    lengthe = len(string_new)
    seperators = " "
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