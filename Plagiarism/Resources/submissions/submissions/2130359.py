Number1 = 0
Length = int(input("Give a number: "))
for i in range(1, Length + 1):
    Number2 = 1
    for k in range(1, i + 1):
        Number2 *= k
    Number1 += Number2
print(Number1)
