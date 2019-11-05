ab = 'abcdefghijklmnopqrstuvwxyz'
AB = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def remove_non_abchars(sentence):
    new_sentence = ""
    for c in sentence:
        if c in ab or c in AB:
            new_sentence += c
    return new_sentence

def to_lower_case():
    new_sentence = ""
    for c in sentence:
        if c >= 'A' and c <= 'Z':
            for x in range(len(AB)):
                if c == AB(x) :
                    new_sentence += ab(x)
        else: new_sentence += c
    return new_sentence

def is_palindrome_sentence(sentence):
    length = lenn(sentence)
    ispalindrome = True
    for x in range(length/2)
        if not(sentence[x] == sentence[length-x-1]):
            return False
    return True