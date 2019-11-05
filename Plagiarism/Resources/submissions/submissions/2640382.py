def encode(s):
    seq = ""
    if s == "X" or s == " ":
        return "0"
    if s == "":
        return
    
    if s[1] == "X":
        seq += "1"
    elif s[1] == " ":
        seq += "0"
    
    for i in range(1, len(s) - 1):
        if s[i - 1] == " " and s[i + 1] == " ":
            seq += "0"
        elif (s[i - 1] == " " and s[i + 1] == "X") or (s[i + 1] == " " and s[i - 1] == "X"):
            seq += "1"
        else:
            seq += "2"
    
    if s[-2] == "X":
        seq += "1"
    elif s[-2] == " ":
        seq += "0"
    
    return seq

def decode(s):
    pass