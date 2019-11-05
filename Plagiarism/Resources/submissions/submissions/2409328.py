n = input("oke")
mogelijkheid = ""

def mogelijkecombinaties(mogelijkheid,n):
    if int(n) > len(mogelijkheid):
        mogelijkheid += "A" 
        mogelijkecombinaties(mogelijkheid)
        
        mogelijkheid += "C" 
        mogelijkecombinaties(mogelijkheid)
        
        mogelijkheid += "G" 
        mogelijkecombinaties(mogelijkheid)
        
        mogelijkheid += "T" 
        mogelijkecombinaties(mogelijkheid)
        
        
    if int(n)== len(mogelijkheid):
        print (mogelijkheid)
        
        
mogelijkecombinaties(mogelijkheid,n)