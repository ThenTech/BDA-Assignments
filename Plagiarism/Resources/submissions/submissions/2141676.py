woord1 = input("Geef een woord: ")
woord2 = input("Geef een woord: ")

for i in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:
    x = 0
    y=0
    sum1 = 0
    sum2 = 0
    while x < len(woord1):
        if woord1[x] == i:
            sum1 = sum1+1
        x = x+1
    while y < len(woord2):
        if woord2[y] == i:
            sum2 = sum2+1
        y = y+1
    if sum1 != sum2:
        break
if i == "z":
    print(woord1 + " and " + woord2 + " are anagrams")
else:
    print(woord1 + " and " + woord2 + " are not anagrams")