def trivial_case(s):
    if s == "X" or s == " ":
        return "0"

def begin_case(s):
    if len(s) > 1:
        if (s[0] == " " and s[1] == "X") or (s[0] == "X" and s[1] == "X"):
            x1 = "1"
            return x1
        elif (s[0] == " " and s[1] == " ") or (s[0] == "X" and s[1] == " "):
            y1 = "0"
            return y1

def end_case(s):
    if len(s) > 1:
        if (s[len(s) - 2] == "X" and s[len(s) - 1] == " ") or (s[len(s) - 2] == "X" and s[len(s) - 1] == "X"):
            print(1, end = "")
            x2 = "1"
            return x2
        elif (s[len(s) - 2] == " " and s[len(s) - 1] == " ") or (s[len(s) - 2] == " " and s[len(s) - 1] == "X"):
            print(0, end = "")
            y2 = "0"
            return y2

def encode(s):
    string = ""
    trivial_case(s)
    string = string + begin_case(s)
    for i in range(1,len(s) - 1):
        if (s[i-1] == " " and s[i+1] == " "):
            string = string + "0"
        elif (s[i-1] == " " and s[i+1] == "X") or (s[i-1] == "X" and s[i+1] == " "):
            string = string + "1"
        else:
            string = string + "2"
    string = string + end_case(s)

def decode(s):
    pass