sentence1 = input("write a sentence ")
sentence2 = input("write a sentence ")
x = 0
y = 0
check = True
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
count1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
count2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
while x < len(sentence1):
    for y in range(27):
        if sentence1[x] == letters[y]:
            count1[y] += 1
    x += 1
x = 0
while x < len(sentence2):
    for y in range(27):
        if sentence2[x] == letters[y]:
            count2[y] += 1
    x += 1
for y in range(26):
    if count1[y] != count2[y]:
        check = False
if check:
    print(sentence1, " and " ,sentence2, " are anagrams", sep="")
else:
    print(sentence1, " and ", sentence2, " are not anagrams", sep="")