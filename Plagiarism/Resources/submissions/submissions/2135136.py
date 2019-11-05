w1 = input("Word 1: ")
w2 = input("Word 2: ")

w1_letters = {"a": 0,
              "b": 0,
              "c": 0,
              "d": 0,
              "e": 0,
              "f": 0,
              "g": 0,
              "h": 0,
              "i": 0,
              "j": 0,
              "k": 0,
              "l": 0,
              "m": 0,
              "n": 0,
              "o": 0,
              "p": 0,
              "q": 0,
              "r": 0,
              "s": 0,
              "t": 0,
              "u": 0,
              "v": 0,
              "w": 0,
              "x": 0,
              "y": 0,
              "z": 0}

w2_letters = {"a": 0,
              "b": 0,
              "c": 0,
              "d": 0,
              "e": 0,
              "f": 0,
              "g": 0,
              "h": 0,
              "i": 0,
              "j": 0,
              "k": 0,
              "l": 0,
              "m": 0,
              "n": 0,
              "o": 0,
              "p": 0,
              "q": 0,
              "r": 0,
              "s": 0,
              "t": 0,
              "u": 0,
              "v": 0,
              "w": 0,
              "x": 0,
              "y": 0,
              "z": 0}
i = 0

while i < len(w1):
    letter = w1[i]
    if letter != " ":
        w1_letters[letter] += 1
    i += 1

i = 0

while i < len(w2):
    letter = w2[i]
    if letter != " ":
        w2_letters[letter] += 1
    i += 1

if w1_letters == w2_letters:
    print("{w1} and {w2} are anagrams".format(w1=w1, w2=w2))
else:
    print("{w1} and {w2} are not anagrams".format(w1=w1, w2=w2))