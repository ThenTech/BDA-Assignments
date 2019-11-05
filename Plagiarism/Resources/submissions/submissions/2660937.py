def coll(w, l, word=""):
    word += w[0] + " "
    if len(w) > 1:
        coll(w[1:], l, word[0: len(word)-2])
        coll(w[1:], l, word)
    if len(word) == l*2:
        print(word[:len(word)-1])


max = int(input("."))
length = int(input("."))
word = ""
if length > 0:
    for i in range(1, max+1):
        word += str(i)
    if len(word) > 0:
        coll(word, length)