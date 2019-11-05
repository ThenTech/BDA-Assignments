def substring(word,start,end):
    subword = ""
    for x in range (start,start + end):
        subword += word[x]
    return subword

def find_pos(word, sentence):
    for x in range(len(sentence)):
        if word[0] == sentence[x]:
            return x