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
letters =""
for i in x:
    if i in y:
        letters += i
if letters ==x:       
    print (True)
else:
    print(False)
        