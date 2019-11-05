punctuation_and_number = '''123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ '''

def is_palindrome_sentence(sentence):
    string_without_punct = ""
    for letter in sentence:
        if letter not in punctuation_and_number:
            string_without_punct = string_without_punct + letter
    ss = string_without_punct.lower()

    ln_ss = int(len(ss))//2
    a = True
    for i in range(ln_ss):
        if ss[i] != ss[len(ss)-1-i] and a == True:
            a = False
    return a
