var_n = input("n")
var_m = input("m")

varvorige = ""

def maaksubsets(varvorige,x,y):
    for i in range (y, x):
        varvorige += str(i)
        if y > 1:
            varvorige += " "
            maaksubsets(varvorige,x-1,y-1)
        if y==1:
            print (varvorige)

maaksubsets(varvorige,int(var_n)+1,int(var_m))