import string

def is_palindrome_sentence(string):
    x = 0
    while x < len(string) -1:
        if string[0+x] == string[len(string)-1-x]:
            x +=1
            return True
        else:
            return False
print(is_palindrome_sentence("nigger"))