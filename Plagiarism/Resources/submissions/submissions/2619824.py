def count_words(string):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    wordcount = 0
    word = ""
    
    while count < len(string):
        if string[count] in alfabet:
            word += string[count]
            count += 1
            continue
        elif len(word) == 0:
            count += 1
            continue
        else:
            wordcount += 1
            word =""
            count += 1
    
    return wordcount