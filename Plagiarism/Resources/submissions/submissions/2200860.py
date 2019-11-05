def encode(s):
    lengthe = len(s)
    teller = 0
    for i in range(lengthe):
        teller = 0
        if i == 0:
            if s[1]=="X":
                teller =1
            else:
                teller =0
        elif i == lengthe-1:
            if s[1]=="X":
                teller =1
            else:
                teller =0
        else:
            if s[i-1] == "X":
                teller +=1
            if s[i+1] == "X":
                teller +=1
        new =""
        new += str(teller)
    if i == lengthe:
        return str(new)
def decode(s):
    pass