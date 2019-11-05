w1 = input()
w2 = input()
for i in range(len(w1)):
    for j in range(len(w2)):
        if w1[i]==w2[j]:
            w2 = w2[:j]+w2[j+1:]
if len(w2) == 0:
    print(w1 ,"and",w2,"are anagrams")
else:
    print(w1 ,"and",w2,"are not anagrams")
            