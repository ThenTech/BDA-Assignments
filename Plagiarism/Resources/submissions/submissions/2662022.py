def encode(s):
    string = ""
    for i in range(len(s)):
        if len(s) == 1:
            string = "0"
        elif i == 0:
            if s[i+1] == "X":
                string += "1"
            else:
                string += "0"
        elif i == len(s)-1:
            if s[i-1] == "X":
                string += "1"
            else:
                string += "0"
        else:
            if s[i-1] == "X" and s[i+1] == "X":
                string += "2"
            elif (s[i-1] == "X" and s[i+1] == " ") or (s[i+1] == "X" and s[i-1] == " "):
                string += "1"
            else:
                string += "0"
    return string



def decode(s, n):
    pass