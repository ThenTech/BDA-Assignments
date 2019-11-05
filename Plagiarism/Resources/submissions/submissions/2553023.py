string1 = str(input("string1:"))
string2 = str(input("string2:"))
alfabet = "abcdefghijklmnopqrstuvwxyz"

for i in alfabet:
    aantal1 = 0
    aantal2 = 0
    for x in range(len(string1)):
        if i == string1[x]:
            aantal1 += 1
        if i == string2[x]:
            aantal2 += 1
    if aantal1 == aantal2:
        continue
    else:
        print(string1, "and", string2, "are not anagrams")
        quit()
print(string1, "and", string2, "are anagrams")