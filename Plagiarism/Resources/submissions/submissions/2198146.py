alfabet = "abcdefghijklmnopqrstuvwxyz"
def is_palindrome_sentence(sentence):
    x = 1
    zin = sentence.split()
    while True:
        if zin[x-1] == zin[len(zin)-x] :
            x = x+1
            return True
        elif zin[x-1] != zin[len(zin)-x] :
            return False
print(is_palindrome_sentence("sentence"))