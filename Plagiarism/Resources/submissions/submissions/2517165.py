var_n = input("n")
var_m = input("m")

varvorige = ""

def maaksubsets(varvorige,x,y):
    if y==0:
        print(varvorige)
    for i in range (y, x):
        if y > 1:
            maaksubsets(varvorige + str(i)+" ",i,y-1)
        if y==1:
            print (varvorige + str(i))
        

maaksubsets(varvorige,int(var_n)+1,int(var_m))