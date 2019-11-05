def remove_punctuation(s):
    s_without_punct = ''
    for letter in s:
        if letter not in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            if letter not in '“”’':
                s_without_punct += letter
        
    return s_without_punct

words = input()
words = remove_punctuation(words)
words = words.split()

for i in words:
   print(i, len(i))