sentence = input("Give a sentence")
x = ""
z = ""
for i in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
          "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]:
    j = 0
    count = 0
    while j < len(sentence):
        if sentence[j] == i:
            count += 1
        j += 1
    x += str(count)
sentence2 = input("Give a second sentence")
for i in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
          "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]:
    j = 0
    count = 0
    while j < len(sentence2):
        if sentence2[j] == i:
            count += 1
        j += 1
    z += str(count)
if x == z:
    print(sentence, "and", sentence2, "are anagrams")
else:
    print(sentence, "and", sentence2, "are not anagrams")

