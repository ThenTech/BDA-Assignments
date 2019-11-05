string = input("Getal: ")
getallen_apart = []

for ch in string:
    getallen_apart.append(ch)

for ch in range(len(getallen_apart)):
    getallen_apart[ch] = int(getallen_apart[ch])

teller = 0
for ch in getallen_apart:
    if ch % 2 == 0:
        teller += 1

print(teller)