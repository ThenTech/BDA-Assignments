x = str(input())
y= str(input())
lettersx = ""
def functie (string):
    for i in x:
        if "a"<=i<="z":
            lettersx = lettersx +i
    return (lettersx)
x=functie(x)
y=functie(y)
for i in x:
    if i in y:
        y=y-i
        x=x-i
if y ==0and x==0:        
    print (True)
else:
    print(False)
        
            
        