def encode(s):
    lengthe = len(s)
    teller = 0
    new = ""
    if s[0] == "X":
        teller +=1
    for i in range(1,lengthe):
        teller = 0
        if i == lengthe:
            if s[i-1] == "X":
                teller +=1
        elif s[i+1] == "X":
            teller +=1
        elif s[i-1] == "X":
            teller +=1
    new += str(teller)
    
    


def decode(s):
    pass