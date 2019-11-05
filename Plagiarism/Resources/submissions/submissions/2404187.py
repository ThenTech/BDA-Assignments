varalf = "abcdefghijklmnopqrstuvwxyz"

def encodeletter(s,n,d):
    for i in range (0,26):
        if i>25:
            return False
        if varalf[j]==s:
            if d==e:
                k=i+int(n)
            if d==d:
                k=i-int(n)
                
        while k>25 or k<0:
            if k>25:
                k-=26
            elif k<0:
                k+=26
        return varalf[k] 


def encode(s, n):
    for j in range (0,len(s)):
        if encodeletter(s[j],n,"e")!=False:
            s= s[0:j]+encodeletter(s[j],n,"e")+s[j+1:len(s)]
        


def decode(s, n):
    for j in range (0,len(s)):
        if encodeletter(s[j],n,"d")!=False:
            s= s[0:j]+encodeletter(s[j],n,"d")+s[j+1:len(s)]