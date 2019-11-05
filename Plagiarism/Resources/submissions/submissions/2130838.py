x = int(input())
y = int(input())
count = 0

for i in range(y):
    outputtext = ""
    for j in range(x):
        if j != 0:
            outputtext += " "
        count += 1
        outputtext += str(count)

    print(outputtext)
