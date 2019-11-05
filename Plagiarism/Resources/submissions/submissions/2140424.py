sentence = input("Give a sentence")
for i in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
          "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]:
    j = 0
    count = 0
    while j < len(sentence):
        if sentence[j] == i:
            count += 1
        j += 1
    print(i + ":", count)
