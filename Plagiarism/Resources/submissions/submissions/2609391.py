woord1 = input()
woord2 = input()
alfabet = "abcdefghijklmnopqrstuvxwyz"
for i in alfeabet:
    tel1 =0
    tel2 = 0
    for j in woord1:
        if j ==i:
            tel1 += 1
    for h in woord2:
        if h == i:
            tel2 +=1
    if tel2 != tel1 :
        print(woord1,"and",woord2,"are not anagrams")
print(woord1,"and",woord2,"are not anagrams")