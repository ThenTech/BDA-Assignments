def cleanup_spaces(s):
    result = ""
    teller = 0
    teller2 = 0
    teller3 = 0
    for i in s:
        if teller3 == (len(s)-1):
            if s[teller3] == " ":
                result = result[:len(result)-1]
                continue
        if teller == 0:
            if i == " ":
                teller3 += 1
                continue
            elif i != " ":
                teller += 1
        if i == " ":
            teller2 += 1
            if teller2 == 1:
                result += i
                teller3 += 1
                continue
            else:
                teller3 += 1
                continue
        teller3 += 1
        teller2 = 0
        result += i
    return result