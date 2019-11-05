x = int(input())
y = int(input())
output = 1
for row in range(0, y):
    for column in range(0, x):
        print(output, end=" ")
        output+= 1
    print()
