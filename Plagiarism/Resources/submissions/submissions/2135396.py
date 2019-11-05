# write your code here

string1 = input("string1: ")
string2 = input("string2: ")

i = 0
y = 0


while i+1 <= len(string1):
    Char_string1 = string1[i]
    if Char_string1 == " ":
        i += 1
        continue
    while y+1 <= len(string2):
        if i+1 == len(string1) and Char_string1 != string2[y]:
            print(string1,"and", string2, "are not anagrams")
        y += 1
    i += 1
    
if (i+1) > len(string1):
    print(string1,"and", string2, "are anagrams")