# write your code here

kolommen = int(input("kolommen:"))
rijen = int(input("rijen"))

x = 1

for i in range(rijen):
    for y in range(kolommen):
        print(x, end=" ")
        x = x + 1
    print()        