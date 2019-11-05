n = input("oke")
mogelijkheid = ""

def mogelijkecombinaties(mogelijkheid,n):
    if int(n) > len(mogelijkheid):
        mogelijkheid += "A" 
        mogelijkecombinaties(mogelijkheid,n)
        
        mogelijkheid += "C" 
        mogelijkecombinaties(mogelijkheid,n)
        
        mogelijkheid += "G" 
        mogelijkecombinaties(mogelijkheid,n)
        
        mogelijkheid += "T" 
        mogelijkecombinaties(mogelijkheid,n)
        
        
    if int(n)== len(mogelijkheid):
        print (mogelijkheid)
        
        
mogelijkecombinaties(mogelijkheid,n)