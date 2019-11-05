alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def count_words(string):
    if string=="":
        words =0
    elif string[0] in alfabet:
        words = 1
    else: 
        words = 0
    i=0
    while i != len(string):
        while string[i] in alfabet:
            i+=1
            if i == len(string):
                return words
        if string [i -1] in alfabet:
            words = words +1
        i = i +1
    return words
print(count_words(""))