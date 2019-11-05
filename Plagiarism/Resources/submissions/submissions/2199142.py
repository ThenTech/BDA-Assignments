sentence = input("give a sentence: "):
    sentencewithoutpunc = ""
    for char in sentence:
        if char in """0123456789!\#$%&'()"*+,-./:;<=>?@[\]^_`{|}~':""":
            sentencewithoutpunc += " "
        else:
            sentencewithoutpunc += char
    splitsentence = sentencewithoutpunc.split()
    for i in range(len(splitsentence)):\
        print(splitsentence[i], len(splitsentence[i]))