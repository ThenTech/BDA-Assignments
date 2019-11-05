x = input()
alpha = "abcdefghijklmnopqrstuvwxyz"
count = 0
for i in x:
    if i in alpha:
        count+=1
    print(i, ":", count)