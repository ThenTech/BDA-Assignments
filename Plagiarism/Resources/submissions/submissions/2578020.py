def cleanup_spaces(s):
    alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,!?.;"
    plaatsen_met_letterofcijfer = list()
    alfabetteller = 0
    resultaat = ""
    for i in s:
        if i in alfabet:
            plaatsen_met_letterofcijfer.append(alfabetteller)
        alfabetteller += 1
    teller = 0
    if len(plaatsen_met_letterofcijfer) == 0:
        return resultaat
    for i in s:
        if i == " ":
            if teller < plaatsen_met_letterofcijfer[0]:
                teller += 1
                continue
            elif teller > plaatsen_met_letterofcijfer[len(plaatsen_met_letterofcijfer)-1]:
                teller += 1
                continue
            elif s[teller+1] == " ":
                teller += 1
                continue
            else:
                resultaat += i
                teller += 1
        else:
            resultaat += i
            teller += 1
    return resultaat