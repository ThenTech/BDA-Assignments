x = input("Geef een niet lege string: ")
i = 0
for i in range(len(x)):
    print(x[len(x) - 1 - i], end="")
print()