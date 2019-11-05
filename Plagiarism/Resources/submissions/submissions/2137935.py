w_1 = input()
w_2 = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
ammountw1 = 00000000000000000000000000
ammountw2 = 00000000000000000000000000

for i in range(len(w_1)):
    for j in range(len(alphabet)):
        if w_1[i] == alphabet[j]:
            ammountw1 += 10**j
            break

for i in range(len(w_2)):
    for j in range(len(alphabet)):
        if w_2[i] == alphabet[j]:
            ammountw2 += 10**j
            break

if ammountw1 == ammountw2:
    print(w_1,'and',w_2,'are anagrams')
else:
    print(w_1,'and',w_2,'are not anagrams')