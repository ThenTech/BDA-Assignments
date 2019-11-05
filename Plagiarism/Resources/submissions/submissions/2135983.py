w1 = input("Word 1: ")
w2 = input("Word 2: ")

w1_letters = {"a":0,"A":0,
              "b":0,"B":0,
              "c":0,"C":0,
              "d":0,"D":0,
              "e":0,"E":0,
              "f":0,"F":0,
              "g":0,"G":0,
              "h":0,"H":0,
              "i":0,"I":0,
              "j":0,"J":0,
              "k":0,"K":0,
              "l":0,"L":0,
              "m":0,"M":0,
              "n":0,"N":0,
              "o":0,"O":0,
              "p":0,"P":0,
              "q":0,"Q":0,
              "r":0,"R":0,
              "s":0,"S":0,
              "t":0,"T":0,
              "u":0,"U":0,
              "v":0,"V":0,
              "w":0,"W":0,
              "x":0,"X":0,
              "y":0,"Y":0,
              "z":0,"Z":0,
              }
w2_letters = {"a":0,"A":0,
              "b":0,"B":0,
              "c":0,"C":0,
              "d":0,"D":0,
              "e":0,"E":0,
              "f":0,"F":0,
              "g":0,"G":0,
              "h":0,"H":0,
              "i":0,"I":0,
              "j":0,"J":0,
              "k":0,"K":0,
              "l":0,"L":0,
              "m":0,"M":0,
              "n":0,"N":0,
              "o":0,"O":0,
              "p":0,"P":0,
              "q":0,"Q":0,
              "r":0,"R":0,
              "s":0,"S":0,
              "t":0,"T":0,
              "u":0,"U":0,
              "v":0,"V":0,
              "w":0,"W":0,
              "x":0,"X":0,
              "y":0,"Y":0,
              "z":0,"Z":0,
              }

i = 0

while i < len(w1):
    letter = w1[i]
    if letter in w1_letters:
        w1_letters[letter] += 1
    i += 1

i = 0

while i < len(w2):
    letter = w2[i]
    if letter in w2_letters:
        w2_letters[letter] += 1
    i += 1

if w1_letters == w2_letters:
    print("{w1} and {w2} are anagrams".format(w1=w1, w2=w2))
else:
    print("{w1} and {w2} are not anagrams".format(w1=w1, w2=w2))