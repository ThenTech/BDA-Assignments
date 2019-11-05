n = input("oke")
mogelijkheid = ""

def mogelijkecombinaties(mogelijkheid,n):
    if int(n) > len(mogelijkheid):
        mogelijkheid = mogelijkecombinaties(mogelijkheid,n)
        mogelijkheid += "A" 
        
        mogelijkheid = mogelijkecombinaties(mogelijkheid,n)
        mogelijkheid += "C" 

        mogelijkheid = mogelijkecombinaties(mogelijkheid,n)
        mogelijkheid += "G" 

        mogelijkheid = mogelijkecombinaties(mogelijkheid,n)
        mogelijkheid += "T" 

        
        
    if int(n)== len(mogelijkheid):
        print (mogelijkheid)
        
        
mogelijkecombinaties(mogelijkheid,n)