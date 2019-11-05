woord = input("Geef een woord: ")
s = ""
for i in range(len(woord)):
    s += woord[len(woord)-1-i]
print(s)
    