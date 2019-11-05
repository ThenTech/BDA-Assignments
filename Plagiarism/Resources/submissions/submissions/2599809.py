x = input("x")
a = input("y")
y = ""

for i in range(len(a)):
    if a[i] == " ":
        continue
    else:
        y += a[i]
for i in x:
    counter = 0
    booly = True
    for j in y:
        if i == " ":
            continue
        elif i != j and booly:
            counter +=1
        elif i == j and booly:
            y = y[:counter]+y[counter+1:]
            booly = False
if y == "":
    print(x, "and", a, "are anagrams")
else:
    print(x, "and", a, "are not anagrams")





