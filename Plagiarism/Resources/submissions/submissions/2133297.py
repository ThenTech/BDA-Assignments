getalx = int(input("Getal : "))

som = 0
term = 0
for x in range(1, getalx+1):
    term += x
    som += term
print(int(som))