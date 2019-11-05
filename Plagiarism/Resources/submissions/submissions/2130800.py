getal = int(input())
tussen_uitkomst = 0
uitkomst = 0
for x in range(1,getal+1):
    uitkomst = uitkomst + tussen_uitkomst
    tussen_uitkomst = 1
    for y in range(1,x+1):
        tussen_uitkomst = tussen_uitkomst * y
uitkomst = uitkomst+tussen_uitkomst
print(uitkomst)