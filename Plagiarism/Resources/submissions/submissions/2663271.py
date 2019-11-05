# write your code here
inputstr = input("word?/sentence?")
letters = "abcdefghijklmnopqrstuvwxyz"
for characters in letters:
    if characters in inputstr:
        countchar = inputstr.count(characters)
        print(characters, ": ", countchar, sep="")
    else:
        print(characters, ": 0",sep="")