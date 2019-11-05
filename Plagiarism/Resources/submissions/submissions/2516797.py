var_n = input("n")
var_m = input("m")

varvorige = ""

def maaksubsets(varvorige,var_n,var_m):
    for i in range (0, var_n):
        varvorige += str(i)
        if len(varvorige) <= (varm*2)-1:
            varvorige+=" "
            maaksubsets(varvorige,var_n,var_m)
        else:
            print (varvorige)