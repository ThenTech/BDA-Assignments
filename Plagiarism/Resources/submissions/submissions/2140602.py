string = input("Word:")
def reverse(string):
    revstring = ""
    index = len (string)
    while index > 0:
        revstring += string[iindex-1]
        index = index-1
    return revstring
print(reverse(string))