y = int(input("Geef het aantal kolommen van de matrix"))
x = int(input("Geef het aantal rijen van de matrix"))

for i in range(1,x+1):
    for j in range(1,y+1):
        print(j+(i-1)*y, end=" ")
    print()