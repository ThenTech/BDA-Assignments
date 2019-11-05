punctuation_and_number = '''123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~'''

def count_words(string):
    string_without_punct = ""
    for letter in string:
        if letter not in punctuation_and_number:
            string_without_punct = string_without_punct + letter
        else:
            string_without_punct = string_without_punct + " "
    wds = string_without_punct.split()
    return len(wds)

print(count_words("one two"))
