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
                if y == len(word) - 1:
                    return x