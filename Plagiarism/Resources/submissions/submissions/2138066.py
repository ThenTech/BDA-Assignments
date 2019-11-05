alphabet = "abcdefghijklmnopqrstuvwxyz"
word1 = input("Enter your word: \n")
word2 = input("Enter your word: \n")

sum = 0

count1 = ""
count2 = ""

for i in range(len(alphabet)):
    for j in range(len(word1)):
        if word1[j] == alphabet[i]:
            sum += 1
    count1 += str(sum)
    sum = 0

for i in range(len(alphabet)):
    for j in range(len(word2)):
        if word2[j] == alphabet[i]:
            sum += 1
    count2 += str(sum)
    sum = 0

print(count1, count2)
if count1 == count2:
    print(word1 + " and " + word2 + " are anagrams")
else:
    print(word1 + " and " + word2 + " are not anagrams")
