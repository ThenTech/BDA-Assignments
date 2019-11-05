sentence1 = input("Please enter the first sentence")
sentence2 = input("Please enter the second sentence")
alphabet = "abcdefghijklmnopqrstuvwxyz"
aantal_letters1 = 0
aantal_letters2 = 0
aantal_gelijk = 0

for i in alphabet:
    aantal1 = 0 
    aantal2 = 0
    for k in sentence1:
        if i == k:
            aantal1 += 1
            aantal_letters1 += 1
    for s in sentence2:
        if i == s:
            aantal2 += 1
            aantal_letters2 += 1
    if aantal1 == aantal2:
        aantal_gelijk += 1
    else:
        break
if aantal_gelijk == aantal_letters1 and aantal_gelijk == aantal_letters2:
    print(sentence1, "and", sentence2, "are anagrams")
else:
    print(sentence1, "and", sentence2, "are not anagrams")