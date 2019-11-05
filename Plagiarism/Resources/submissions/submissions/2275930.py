def decode(s):
    a1 = "X"
    a2 = " "
    #stap 1
    if s[0] == "1":
        a1 += "X"
    elif s[0] == "0":
        a1 += " "
    #stap 2
    i = 2 #a1
    while i < len(s):
        if s[i - 1] == "1" and a1[len(a1)-2]== " ":
            a1 += "X"
            i += 1
        elif s[i - 1] == "1" and a1[len(a1) - 2] == "X":
            a1 += " "
            i += 1
        elif s[i-1] == "2": #bij 2x
            a1 += "X"
            i += 1
        elif s[i-0] == "0": #bij 0x
            a1 += " "
            i += 1
    i = 2 #a2
    while i < len(s):
        if s[i - 1] == "1" and a2[len(a2) - 2] == " ":
            a1 += "X"
            i += 1
        elif s[i - 1] == "1" and a2[len(a2) - 2] == "X":
            a2 += " "
            i += 1
        elif s[i - 1] == "2":  # bij 2x
            a2 += "X"
            i += 1
        elif s[i - 0] == "0":  # bij 0x
            a2 += " "
            i += 1

    return a1, a2