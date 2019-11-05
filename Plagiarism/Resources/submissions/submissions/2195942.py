def check_punc(sentence):
    word = ""
    for i in sentence:
        if i in """,?!. ""';:/""":
            pass
        else:
            word += i
    return word



def is_palindrome_sentence(sentence):
    check = True
    sentence1 = sentence.lower()

    word = check_punc(sentence1)
    for i in range(0, len(word)):
        if word[i] != word[len(word)-1-i]:
            return False
    return True