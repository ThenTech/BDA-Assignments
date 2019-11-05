n = input("oke")
mogelijkheid = ""

def mogelijkecombinaties(i,j):
    eerste_getal = i*2-1
    tweede_getal = j*2
    
    if eerste_getal < len(n) or tweede_getal > eerste_getal:
        print (n[eerste_getal:tweede_getal])
    else:
        return ""
    mogelijkecombinaties(i+1,j)
    mogelijkecombinaties(i,j-1)
    
mogelijkecombinaties(0,len(n))

