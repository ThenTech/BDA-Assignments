def is_palindrome_sentence(sentence):
    oneword = ""
    for char in sentence:
        if char in """0123456789!\#$%&'()"*+,-./:;<=>?@[\]^_`{|}~': """:
            oneword += ""
        else:
            oneword += char
    onewordlower = oneword.lower()
    mirror= ""
    for i in range(0,len(onewordlower)):
        mirror = onewordlower[i] +mirror
    if onewordlower == mirror:
        print(True)

is_palindrome_sentence("A man, a plan, a canal: Panama.")