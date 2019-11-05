inputString = str(input())
outputString = ""
for i in range(len(inputString), 0, -1):
    outputString += inputString[i-1]

if (inputString == outputString):
    print(inputString, "is a palindrome")
else:
    print(inputString, "is not a palindrome")
