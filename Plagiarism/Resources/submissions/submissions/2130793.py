getalx = input("mag ik x graag")

getalx = int(getalx)
plusget = 0
tussenuitkomst = 0
i=1
uitkomst = 0

for i in range (getalx):
    for j in range (i):
        plusget += 1
        tussenuitkomst += plusget
    uitkomst += tussenuitkomst
print(uitkomst)