x = int(input("x = ?\n"))   # 7
y = int(input("y = ?\n"))   # 5

for i in range(1, y+1):
    for j in range((i-1)*x+1, x*i+1):
        print(str(j) + " ", end="")
    print()

