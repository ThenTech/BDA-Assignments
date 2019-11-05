def count_words(strWord):
    Punc = " .,:!?0123456789"

    blnPunc = False
    Counter = 0

    for intC in range(0, len(strWord)):
        Char = strWord[intC]

        if Char in Punc:
            if(not blnPunc):
                Counter += 1

            blnPunc = True
        else:
            blnPunc = False

    if (not blnPunc):
        Counter += 1

    return Counter