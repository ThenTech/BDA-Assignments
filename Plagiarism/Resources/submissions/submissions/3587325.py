def encode(s):
    mineField = ""
    for i in range(len(s)):
        if i == 0:
            if s[i+1] == 'X':
                mineField += "1"
            else:
                mineField += "0"
        elif i == len(s) - 1:
            if s[i-1] == "X":
                mineField += "1"
            else:
                mineField += "0"
        else:
            if s[i-1] == "X" and s[i+1] == "X":
                mineField += "2"
            elif s[i-1] == "X" and s[i+1] == " " or s[i-1] == " " and s[i+1] == "X":
                mineField += "1"
            else:
                mineField += "0"
    return mineField

def decode(s):
    pass