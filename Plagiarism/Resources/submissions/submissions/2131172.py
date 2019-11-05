x = int(input("Geef me een waarde voor x: "))
r = 1
g = 0
for i in range(1, x+1):
    r = r * i
    g = g + r
print(g)