x = int(input("Geef me een waarde voor x: "))
y = int(input("Geef me een waarde voor y: "))
r = 1
g = 1
v = 1
for i in range (1,x+1):
    r = r * i
for j in range(1,y+1):
    g = g * j
for p in range(1,x-y+1):
    v = v*p
print(r/(g*v))