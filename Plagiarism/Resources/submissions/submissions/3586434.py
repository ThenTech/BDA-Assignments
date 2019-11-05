string = input()

reverseString += ""

for i in range(len(string)):
    reverseString += string[len(string) - 1 - i]
    
print(reverseString)