# write your code here
getalX = int(input("geef een getal groter dan 0: "))
resultX = 1
getalY = int(input("geef een tweede getal groter dan 0: "))
resultY = 1

for t in range(1, min(getalY, getalX - getalY) + 1):
    resultX *= getalX
    resultY *= t
    getalX -= 1

print(resultX // resultY)