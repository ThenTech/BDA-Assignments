x = input("word 1?")
y = input("word 2?")
anagram = True
counter_x = 0
counter_y = 0

for i in "abcdefghijklmnopqrstuvwxyz":
    for j in x:
        if j == i:
            counter_x = counter_x+1
    for k in y:
        if k == i:
            counter_y = counter_y+1
    if counter_x == counter_y:
        counter_x = 0
        counter_y = 0
    else:
        anagram = False
        break
if anagram == True:
    print(x, "and", y, "are anagrams")
else:
    print(x, "and", y, "are not anagrams")