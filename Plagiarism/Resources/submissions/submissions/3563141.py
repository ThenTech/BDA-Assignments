string1 = input("give a word or a sentence: ")
string2 = input("give a word or a sentence: ")

test1 = ""
teller = 0
for i in string1:
    if i == " ":
        test1 += ""
        teller += 1
    else:
        test1 += i

test2 =""
for i in string2:
    if i == " ":
        test2 += ""
    else:
        test2 += i
if len(test1) != len(test2):
    print(string1, "and", string2, "are not anagrams")

count = 0
tel = 0

for i in range(len(test1)):
    for j in range(len(test2)):
        if test1[i] == test2[j]:
            count += 1
        if count > 1:
            count = 1
    tel += count

if (tel == len(string1) - teller):
    print(string1, "and", string2, "are anagrams")
else:
    print(string1, "and", string2, "are not anagrams")