x = "abcdefghijklmnopqrstuvwxyz"
y = str(input("Give a sentence: "))
for i in range(0,26):
    print(x[0 + i], ": ", y.count(str(x[0 + i])) ,sep='')