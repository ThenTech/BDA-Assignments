def substring(word,start,end):
    subword = ""
    for x in range (start,start + end):
        subword += word[x]
    return subword

def find_pos(word, sentence):
    check = True
    for x in range(len(sentence)):
        if word[0] == sentence[x]:
            for y in range(len(word)):
                if word[y] != sentence[x + y]:
                    check = False
                    break
                if y + 1 == len(word) and check:
                    return x