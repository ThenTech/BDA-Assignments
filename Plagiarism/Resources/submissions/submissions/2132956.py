x = int(input("Geef een waarde voor x: "))
r = 0
for i in range (x+1):
    for j in range(i+1):
        r = r + j
print(r)