def substring(word,start,end):
    subword = ""
    for x in range (start,start + end):
        subword += word[x]
    return subword

def find_pos(word, sentence):
    for x in range(len(sentence)):
        for y in range(len(word)):
            if word[y] == sentence[x + y]:
                return x