x = int(input())
y = int(input())
for i in range(y):
    outputtext = ""
    for j in range(x):
        outputtext += " " + str(int(j+1)*int(i+1))
    print(outputtext)
