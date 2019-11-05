x = int(input("What is x? "))
y = int(input("What is y? "))

length = [1, x]
print(range(1, x))
print()

a = 0

for vertical in range(y):
    for horizontal in range(1, x + 1):
        a += 1
        print(a, end=" ")
    print("")
