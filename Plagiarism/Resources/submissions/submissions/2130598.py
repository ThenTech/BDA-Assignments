getalx = input("wat is getal x")
getaly = input("wat is getal y")
getalx = int(getalx)
getaly = int(getaly)

i=0

waardee = getaly - 1
uitkomst = 1

for i in range (getaly):
    uitkomst *= (getalx-i)/(getaly-i)
uitkomst = int(uitkomst)
print (uitkomst)