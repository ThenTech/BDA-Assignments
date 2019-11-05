# is_palindrome_sentence("A man, a plan, a canal: Panama.")
alfabet = "azertyuiopqsdfghjklmnbvcxw"
def split_lower(sentence):
    sentence = sentence.lower
    sentence = sentence.split(":")
    return sentence

def nieuwe_string(lijst):
    nieuwe_string = ""
    for el in lijst[0]:
        if el in alfabet:
            nieuwe_string + nieuwe_string + el
    return nieuwe_string

def vgl(eerste, tweede):
    if tweede in eerste:
        return True
    elif tweede not in eerste:
        mirror =""
        for el in range(len(tweede)):
            mirror = mirror + tweede[len(tweede)-1-el]
        if mirror in eerste:
            return True
    else:
        return False


def is_palindrome_sentence(sentence):
    sentence_aangepast = split_lower(sentence)
    nieuwe_string = nieuwe_string(sentence_aangepast)
    return vgl(nieuwe_string, sentence[1])