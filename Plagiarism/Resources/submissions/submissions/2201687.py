alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
woord = input("woord: ")

def functie(s):
    x=0
    z= woord[0]
    while True:
        if woord[x] in alfabet:
            if x>0:
               z = z+woord[x]
            x=x+1
        else:
           print(z, x)
           return False
functie(0)