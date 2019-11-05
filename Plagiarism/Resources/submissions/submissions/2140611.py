alphabet = "abcdefghijklmnopqrstuvwxyz"
input1 = input()
input2 = input()
anagram1 = ''
anagram2 = ''

for i in range(len(alphabet)):
    som1 = 0
    som2 = 0
    for j in range(len(input1)):
        if alphabet[i] == input1[j]:
            som1 += 1
            anagram1 = str(som1)
    for j in range(len(input2)):
        if alphabet[i] == input2[j]:
            som2 += 1
            anagram2 = str(som2)
if anagram1 == anagram2:
    print(input1, 'and', input2, 'are anagrams')
else:
    print(input1, 'and', input2, 'are not anagrams')