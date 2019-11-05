def Count_words(strWord):
    Punc = " .,:!?"
    Num = "0123456789"

    blnNumber = False
    Counter = 0

    for intC in range(0, len(strWord)):
        Char = strWord[intC]

        if Char in Num:
            blnNumber = True
        elif Char in Punc:
            if blnNumber:
                blnNumber = False
            else:
                Counter += 1

    return Counter
