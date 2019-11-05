n = input("n")
m = input("m")
def functie_voornu (n,m):
    n=int(n)
    m=int(m)
    for i in range (m,n+1):
        if m>0:
            teprinten += i + " "
            m-=1
            functie_voornu (n-1,m)
        print (teprinten)
        teprinten = ""

functie_voornu (n,m)    