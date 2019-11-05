x=int(input("Geef het aantal kolommen"))
y=int(input("Geef het aantal rijen"))
for i in range(1,y+1):
    for j in range(x*i-x-1,(x*i+1)):
        print(j,end=" ")
    print()