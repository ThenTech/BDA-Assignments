def words_lengths(sentence):
    woordd = ""
    result = ""
    for i in range(len(sentence)):
        if sentence[i] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            woordd += sentence[i]
        if sentence[i] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" or i == len(sentence)-1:
            if woordd == "":
                continue
            woordd += " " + str(len(woordd))
            print(woordd)
            woordd = ""


words_lengths(str(input("lol: ")))