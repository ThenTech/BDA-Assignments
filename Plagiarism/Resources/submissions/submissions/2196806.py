def count_words(s):
    s_without_punct = ""

    for letter in s:
        if letter in "123456789&é"'(§è!çà)-_,;:=?./+¨*%£^$ùµ<>\~´`[]|@#^{}/*-+':
            s_without_punct += " "
        else:
            s_without_punct += letter

    splitedsentence = s_without_punct.split()
    return len(splitedsentence)


count_words("one two")
