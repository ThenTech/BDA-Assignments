a = int(input())
b = int(input())


for i in range(1, b*(a+1)):
    if i // a == 0:
        print()
    print(i, end = "")
    