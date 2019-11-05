x = input("Geef een zin: ")
alfabet = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(alfabet)):
    count = 0
    for j in range(len(x)):
        if x[j] == alfabet[i]:
            count += 1
    print(alfabet[i] + ":", count)
        
        