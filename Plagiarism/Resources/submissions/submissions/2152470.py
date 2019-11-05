alphabet = "abcdefghijklmnopqrstuvwxyz"
input1 = input()
input2 = input()
anagram1  = ''
anagram2 = ''

for i in range(len(alphabet)):
    som = 0
    for j in range(len(input1)):
        if alphabet[i] == input1[j] and input1 != ' ':
            som = som + 1
    anagram1 = anagram1 + str(som)

for i in range(len(alphabet)):
    som = 0
    for j in range(len(input2)):
        if alphabet[i] == input2[j] and input2 != ' ':
            som = som + 1
    anagram2 = anagram2 + str(som)

if anagram1 == anagram2:
    print(input1, 'and', input2, 'are anagrams')
else:
    print(input1, 'and', input2, 'are not anagrams')