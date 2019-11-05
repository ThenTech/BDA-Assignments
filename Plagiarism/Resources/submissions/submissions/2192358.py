letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def remove(zin):
    new_string = ""
    for i in zin:
        if i in letters:
            new_string += i
        else:
            continue
    return new_string

def is_palindrome_sentence(sentence):
    new_sentence = remove(sentence)
    reversed_sentence = ""
    for i in range(len(new_sentence)):
        reversed_sentence += new_sentence[len(new_sentence)-1-i]
    print(new_sentence.lower())
    print(reversed_sentence.lower())
    if new_sentence.lower() == reversed_sentence.lower():
        return True
    else:
        return False