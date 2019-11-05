n = input("n")
m = input("m")
teprinten=""
def functie_voornu (n,m,tp):
    n=int(n)
    m=int(m)
    for i in range (m,n+1):
        if m>0:
            tp += str(i) + " "
            m-=1
            tp = functie_voornu (n-1,m,tp)
        print (tp)
        tp = tp[0:len(tp)-2]
        return tp

functie_voornu (n,m,teprinten)    