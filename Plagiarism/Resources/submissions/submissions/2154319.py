def substring(word,start,end):
    subword = ""
    for x in range (start,start + end):
        subword += word[x]
    return subword

def find_pos(word, sentence):
    check = True
    z = 0
    for x in range(len(sentence)):
        z = x
        for y in range(len(word)):
            if word[y] != sentence[x + y]:
                check = False
    if check:
        return z   