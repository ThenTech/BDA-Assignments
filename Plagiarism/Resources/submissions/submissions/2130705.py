#input vragen
x = int(input("X:"))
y = int(input("Y:"))
opl = 1
#loop opzetten om berekening uit te voeren
for i in range(y):
    opl = opl * ((x-i)/(y-i))
print(str(opl))