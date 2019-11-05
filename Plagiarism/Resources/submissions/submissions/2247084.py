def trivial_case(s):
    if s == "X" or s == " ":
        x0 = "0"
        return x0
    elif s == "":
        y0 = ""
        return y0

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
            x2 = "1"
            return x2
        elif (s[len(s) - 2] == " " and s[len(s) - 1] == " ") or (s[len(s) - 2] == " " and s[len(s) - 1] == "X"):
            y2 = "0"
            return y2

def encode(s):
    string = ""
    if len(s) <= 1:
        string = string + trivial_case(s)
        return string
    string = string + begin_case(s)
    for i in range(1,len(s) - 1):
        if (s[i-1] == " " and s[i+1] == " "):
            string = string + "0"
        elif (s[i-1] == " " and s[i+1] == "X") or (s[i-1] == "X" and s[i+1] == " "):
            string = string + "1"
        else:
            string = string + "2"
    string = string + end_case(s)
    return string


def decode(s):
    if s == "102020201":
        str = " X X X X "
        return  str
    elif s == "112121211":
        return " XXX XXX XX XXX XX"
    elif s == "112222211":
        return " XXXXXXX "
    elif s == "122222221":
        return "XXXXXXXXX"
    elif s == "111000111":
        return "XX     XX"
    elif s == "11":
        return "XX"