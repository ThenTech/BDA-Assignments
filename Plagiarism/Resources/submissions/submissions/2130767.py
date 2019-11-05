columns = input("What's the first number: ")
rows = input("what's the second number: ")

y = int(columns)
x = int(rows)
a = 0
for i in range(x):
    for b in range(y):
        a = a + 1
        print(a, end=" ")
    print()

