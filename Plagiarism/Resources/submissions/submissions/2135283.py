# write your code here

string1 = input("string1: ")
string2 = input("string2: ")

i = 0
y = 0

if len(string1) != len(string2):
    print(string1,"and", string 2, "are not anagrams")
    exit()

while i+1 <= len(string1):
    Char_string1 = string1[i]
    while y+1 <= len(string2):
        if y+1 = len(string2) and Char_string1 != string2[y]:
            print(string1,"and", string 2, "are not anagrams")
        y += 1
    x += 1
    
if (x+1) > len(string1):
    print(string1,"and", string 2, "are anagrams")