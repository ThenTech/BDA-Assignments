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