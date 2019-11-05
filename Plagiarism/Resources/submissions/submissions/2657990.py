x = input()
alpha = "abcdefghijklmnopqrstuvwxyz"
for i in alpha:
    count = 0
    for j in range(0, len(x)):
        if i==x[i]:
            count+=1
    print(i,":",count)