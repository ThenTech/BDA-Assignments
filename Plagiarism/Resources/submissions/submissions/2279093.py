def encode(s):
    answer = ""
    #deel 1
    if len(s) == 1:
        if s == "X":
            answer += "0"
        else:
            answer += "0"
    if len(s) > 1:
        if s[1] == "X":
            answer += "1"
        else:
            answer += "0"
        #deel 2
        i=1
        while i < len(s)-1:
            if s[i-1] == " " and s[i+1] == "X":
                answer += "1"
                i += 1
            elif s[i-1] == "X" and s[i+1] == " ":
                answer += "1"
                i += 1
            elif s[i-1] == "X" and s[i+1] == "X":
                answer += "2"
                i += 1
            elif s[i - 1] == " " and s[i + 1] == " ":
                answer += "0"
                i += 1
        #deel 3
        if s[len(s)-2] == "X":
            answer += "1"
        else:
            answer += "0"
    return answer


def decode(s):
    a1 = "X"
    a2 = " "
    #stap 1
    if s[0] == "1":
        a1 += "X"
        a2 += "X"
    elif s[0] == "0":
        a1 += " "
        a2 += " "
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
        elif s[i-1] == "0": #bij 0x
            a1 += " "
            i += 1
    i = 2 #a2
    while i < len(s):
        if s[i - 1] == "1" and a2[len(a2) - 2] == " ":
            a2 += "X"
            i += 1
        elif s[i - 1] == "1" and a2[len(a2) - 2] == "X":
            a2 += " "
            i += 1
        elif s[i - 1] == "2":  # bij 2x
            a2 += "X"
            i += 1
        elif s[i - 1] == "0":  # bij 0x
            a2 += " "
            i += 1
    if s[1] == "0" or s[0:4] == "1122":
        print(a2)
    elif len(s) == 2 and s[0:2] == "11":
        print(a1)
    else:
        print(a1)
        print(a2)
