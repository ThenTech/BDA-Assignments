def remove_punctuation(s):
    s_without_punct = ''
    for letter in s:
        if letter in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            s_without_punct += ' '
        if letter not in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            if letter not in '“”’':
                s_without_punct += letter
        
    return s_without_punct

def remove_int(s):
    s_without_int = ''
    for letter in s:
        if letter in '123456789':
            s_without_int += ' '
        if letter not in '123456789':
            s_without_int += letter
    return s_without_int

words = input()
words = remove_punctuation(words)
words = remove_int(words)
words = words.split()

for i in words:
   print(i, len(i))