def convert_to_lowercase(sentence):
    new_sentence = ""
    for letter in sentence:
        if "A" <= letter <= "Z":
            new_number = ord(letter) - ord("A") + ord("a")
            lowercase = chr(new_number)
            new_sentence = new_sentence + lowercase
        else:
            new_sentence = new_sentence + letter
    return new_sentence

def clean_sentence(sentence):
    new_sentence = ""
    for letter in sentence:
        if "a" <= letter <= "z":
            new_sentence = new_sentence + letter
    return new_sentence

def is_palindrome_sentence(sentence):
    sentence = convert_to_lowercase(sentence)
    sentence = clean_sentence(sentence)
    length = len(sentence)
    length_half = length // 2
    i = 0
    a = True

    while i < length_half:
        if sentence[i] in [sentence[length - 1 - i]]:
            a = True
            i = i + 1
        else:
            a = False
            i = length_half + 1
            return False
    if a:
        return True