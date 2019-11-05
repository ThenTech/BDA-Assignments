def cleanup_spaces(s):
    result = ""
    print(len(s))
    teller = 0
    teller2 = 0
    for i in s:
        if teller == 0:
            if i == " ":
                continue
            elif i != " ":
                teller += 1
        if i == " ":
            if i == " ":
                teller2 += 1
                if teller2 == 1:
                    result += i
                    continue
                else:
                    continue
            else:
                result += i
        teller2 = 0
        result += i
    return result