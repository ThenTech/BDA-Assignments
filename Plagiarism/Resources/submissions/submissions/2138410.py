zin = input("Geef een zin.")
alfabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
counter = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
x = 0
for j in alfabet:
    for i in range(0, len(zin)):
        if j == zin[i]:
            counter[x] += 1
        else:
            continue
    print(j, ": ", counter[x])
    x += 1