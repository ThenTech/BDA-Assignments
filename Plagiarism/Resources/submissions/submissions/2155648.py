def substring(word,start,end):
    subword = ""
    for x in range (start,start + end):
        subword += word[x]
    return subword

def find_pos(word, sentence):
    for x in range(len(sentence)):
        check = True
        if word[0] == sentence[x]:
            for y in range(len(word)):
                if word[y] != sentence[x + y]:
                    check = False
                    break
                if y + 1 == len(word) and check:
                    return x

def in_string(word, sentence):
    if find_pos(word, sentence) != None:
        return True
    else:
        return False