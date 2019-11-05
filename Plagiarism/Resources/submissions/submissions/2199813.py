def encode(s):
    lengthe = len(s)
    teller = 0
    for i in range(lengthe):
        teller = 0
        if i == 0:
            if s[1]=="X":
                teller =1
                print(teller, end="")
            else:
                teller =0
                print(teller,end="")
        elif i == lengthe-1:
            if s[1]=="X":
                teller =1
                print(teller,end="")
            else:
                teller =0
                print(teller,end="")            
        else:
            if s[i-1] == "X":
                teller +=1
            if s[i+1] == "X":
                teller +=1
            print(teller,end="")
        new =""
        new += str(teller)
    if i == lengthe:
        return str(new)
def decode(s):
    pass