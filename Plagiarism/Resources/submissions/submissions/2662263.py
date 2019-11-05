x = input("x?")
y = input("y?")

result = 1
for i in range(0, y):
    result = result * ((x - i)/ (y - i))
print(int(result))