woord=input("Geef een woord")
x=0
for i in ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"):
    som=0
    while x<len(woord):
        if woord[x]==i:
            som=som+1
        x=x+1 
    print(i,": ",som)
    continue