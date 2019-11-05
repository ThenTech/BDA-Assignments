def coll(w, l, word=""):
    word += w[0] + " "
    if len(w) > 1:
        coll(w[1:], l, word[0: len(word)-2])
        coll(w[1:], l, word)
    if len(word) == l*2:
        print(word)


max = int(input("."))
length = int(input("."))
word = ""

for i in range(0, max):
    word += str(max-i)
if len(word) > 0:
    coll(word, length)
print()
