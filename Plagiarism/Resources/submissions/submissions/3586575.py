stringA = input()
stringB = input()

alphabetLocation = 0
letter = 97

list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(stringA)):
    if string[i] != " ":
        alphabetLocation = ord(string[i]) - 97
        list[alphabetLocation] += 1
        
for i in range(len(stringB)):
    if string[i] != " ":
        alphabetLocation = ord(string[i]) - 97
        list[alphabetLocation] -= 1
    
while i+1 != len(list):
    if list[i] != 0:
        print(stringA, "and", stringB, "are not anagrams", sep=" ")
        break
    if i == len(list)-1:
        print(stringA, "and", stringB, "are anagrams", sep=" ")
        break;
        
    i += 1
    
