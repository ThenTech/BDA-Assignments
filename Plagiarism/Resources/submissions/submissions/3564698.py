x = int(input("Amount columns: "))
while x < 1:
    x = int(input("Amount columns: "))
y = int(input("Amount rows: "))
while y < 1:
    y = int(input("Amount rows: "))

val = 1
for row in range(y):
    for col in range(x):
        print(val, end=" ")
        val += 1
    print()