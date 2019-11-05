x = input()
y = input()
alfabet = "abcdefghijklmnopqrstuvwxyz"
for i in alfabet:
    teller x = 0
    teller y = 0
    for j in x:
        if j == i:
            tellerx += 1
    for h in y:
        if i == h:
            tellery += 1
    if tellery != tellerx:
        print(x,"and",y,"are not anagrams")
        break
    elif i == "z":
        print(x,"and",y,"are anagrams")