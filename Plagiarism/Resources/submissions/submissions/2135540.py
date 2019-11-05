# write your code here

string1 = input("string1: ")
string2 = input("string2: ")

i = 0
y = 0


while i+1 <= len(string1):
    y = 0
    Char_string1 = string1[i]
    while y+1 <= len(string2):
        if y+1 == len(string1) and Char_string1 != string2[y]:
            print(string1,"and", string2, "are not anagrams")
            exit()
        elif Char_string1 == string2[y]:
            break
        y += 1
    i += 1
    
if (i+1) > len(string1):
    print(string1,"and", string2, "are anagrams")