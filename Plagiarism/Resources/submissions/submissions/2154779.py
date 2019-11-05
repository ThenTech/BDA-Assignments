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
        if word[0] == sentence[x]:
            for y in range(len(word)):
                if word[y] != sentence[x + y]:
                    check = False
                    break
        break
    if check:
        return z