# write your code here
inputstr = input("Word?")

for i in range(len(inputstr)):
    print(inputstr[len(inputstr) - 1 - i], end='')
print()