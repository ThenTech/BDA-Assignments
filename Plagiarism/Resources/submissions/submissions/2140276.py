x = input("Geef een niet lege string: ")
i = 0
while i < len(x):
    print(x[len(x) - i - 1], end="")
    i = i+1