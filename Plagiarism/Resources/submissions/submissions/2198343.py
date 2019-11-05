def is_palindrome_sentence(sentence):
    oneword = ""
    for char in sentence:
        if char in """0123456789!\#$%&'()"*“+,-./:;<”=>?@[\’]^_`{|}~': """:
            oneword += ""
        else:
            oneword += char
    onewordlower = oneword.lower()
    mirror= ""
    for i in range(0,len(onewordlower)):
        mirror = onewordlower[i] +mirror
    if onewordlower == mirror:
        return True
    else:
        return False
is_palindrome_sentence("Are we not pure? “No sir!” Panama’s moody Noriega brags. “It is garbage!” Irony dooms a man; a prisoner up to new era.")