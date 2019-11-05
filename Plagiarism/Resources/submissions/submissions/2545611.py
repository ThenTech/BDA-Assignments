x = input()
y = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(alphabet)):
    countx = 0
    county = 0
    for j in range(len(x)):
        if x[j] == alphabet[i]:
            countx += 1
    for k in range(len(y)):
        if y[k] == alphabet[i]:
            county +=1
    if countx != county:
        print(x, "and", y, "are not anagrams")
        break
    elif i == len(alphabet) - 1:
        print(x, "and", y, "are anagrams")