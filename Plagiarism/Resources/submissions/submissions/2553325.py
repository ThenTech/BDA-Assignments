string1 = str(input("string1:"))
string2 = str(input("string2:"))
alfabet = "abcdefghijklmnopqrstuvwxyz"

string11 = ""
for i in string1:
    if i in alfabet:
        string11 += i

string22 = ""
for i in string2:
    if i in alfabet:
        string22 += i

for i in alfabet:
    aantal1 = 0
    aantal2 = 0
    for x in range(len(string11)):
        if i == string11[x]:
            aantal1 += 1
        if i == string22[x]:
            aantal2 += 1
    if aantal1 == aantal2:
        continue
    else:
        print(string1, "and", string2, "are not anagrams")
        quit()
print(string1, "and", string2, "are anagrams")