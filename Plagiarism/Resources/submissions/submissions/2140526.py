input = str(input())
evenAmount = 0
for i in input:
    if int(i)%2 == 0:
        evenAmount += 1
print(evenAmount)