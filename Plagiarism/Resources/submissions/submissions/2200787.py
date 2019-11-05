def replace(pattern, replacement, corpus):
    teller = 0
    string = ''
    extraStr = ''

    for i in corpus:
        if pattern[teller] == i:
            extraStr += i
            teller += 1
            if extraStr == pattern:
                string += replacement
                teller = 0
                extraStr = ''
        else:
            teller = 0
            string += extraStr
            string += i
            extraStr = ''
    return string