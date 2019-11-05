x = str(input())
y= str(input())
def functie (string):
    letters = ""
    for i in string:
        if "a"<=i<="z":
            letters = letters +i
    return (letters)
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
        