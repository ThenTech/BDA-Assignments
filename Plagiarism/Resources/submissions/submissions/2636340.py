x = input("")
y = input("")
alphabet = "abcdefghijklmnopqrstuvwxyz"
is_anagram = True 

def counter(string, letter):
    count = 0
    for i in range(len(string)):
        if string[i] == letter:
            count += 1
    return count
 
k = 0
while k < len(alphabet):
    if counter(x, alphabet[k]) != counter(y, alphabet[k]):
        is_anagram = False
        break
    k += 1

if is_anagram:
    print(x, "and", y, "are anagrams")
else:
    print(x, "and", y, "are not anagrams")
    


    
    