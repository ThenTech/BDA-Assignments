woord=input("Geef een woord")

for i in ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"):
    x=0
    som=0
    while x<len(woord):
        if woord[x]==i:
            som=som+1
        x=x+1 
    print(i,": ",som)
        