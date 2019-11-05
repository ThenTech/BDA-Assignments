inputString = str(input())
outputString = ""
for i in range(len(inputString),0,-1):
    outputString += inputString[i-1]
print(outputString)# write your code here