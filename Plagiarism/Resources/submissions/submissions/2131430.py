x=input("value x: ")
resultaat =0
for i in range(1,x+1):
    f=1
    for j in range (1, i+1):
        f=j+f
    resultaat=resultaat+f
print(resultaat)