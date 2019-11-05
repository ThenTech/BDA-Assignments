import string
def is_palindrome_sentence(sentence):
    x = sentence.lower()
    #print(x)
    text = ""
    mirror = ""
    for i in x:
        if i not in string.punctuation and i!= " ":
            text += i
    #for j in range(len(text)-1,-1,-1):     kan ook 
    #    mirror += text[j]
    for j in range(len(text)):
        mirror += text[len(text)-1-j]    # let goed op met de -1

    #print(text)
    #print(mirror)
    if text == mirror:
        return True
    else:
        return False