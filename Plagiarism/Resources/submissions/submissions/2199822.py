letters = "abcdefghijklmnopqrstuvwxyz"
def convert_to_uppercase(s):
    newword = ""
    counter = 0
    for i in s:
        if i in letters:
            newword += (chr(ord(s[counter])- 32))
        else:
            newword += (s[counter])
        counter += 1
    return newword