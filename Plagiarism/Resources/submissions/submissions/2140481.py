word_1 = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0
            ,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}

word_2 = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0
            ,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}

inputString_1 = str(input())
inputString_2 = str(input())

for i in range(len(inputString_1),0,-1):
    if inputString_1[i-1] != " " and (inputString_1[i-1] >= "a" and inputString_1 <= "z"):
        word_1[inputString_1[i-1]] += 1

for i in range(len(inputString_2),0,-1):
    if inputString_2[i-1] != " " and (inputString_2[i-1] >= "a" and inputString_2 <= "z"):
        word_2[inputString_2[i-1]] += 1

if word_1 == word_2:
    print (inputString_1, "and", inputString_2, "are anagrams")
else :
    print (inputString_1, "and", inputString_2, "are not anagrams")
