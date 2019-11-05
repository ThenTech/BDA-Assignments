c1 = int(input())
c2 = int(input())
c5 = int(input())
c10 = int(input())
c20 = int(input())
totalc = c1 * 1 + c2 * 2 + c5 * 5 + c10 * 10 + c20 * 20
totale = totalc / 100
if totale < 1:
    print("You have ", totale, 0, " euro!", sep="")
else:
    print("You have ", totale, " euro!", sep="")
