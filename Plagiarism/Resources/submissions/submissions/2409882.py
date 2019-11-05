n = input("oke")
mogelijkheid = ""

def mogelijkecombinaties(mogelijkheid,n):
    if int(n) > len(mogelijkheid):
        n = int(n)
        mogelijkheid = mogelijkecombinaties(mogelijkheid+"A",n-1)

        mogelijkheid = mogelijkecombinaties(mogelijkheid+"C",n-1)

        mogelijkheid = mogelijkecombinaties(mogelijkheid+"G",n-1)
 
        mogelijkheid = mogelijkecombinaties(mogelijkheid+"T",n-1)


        
        
    if int(n)== 0:
        print (mogelijkheid)
        
        
mogelijkecombinaties(mogelijkheid,n)