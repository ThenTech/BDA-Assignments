def encode(s):
    snew = " " + s + " "
    n = 0
    output = ""
    for i in range (1,len(snew) - 1):
        n = 0
        if snew[i-1]=="X":
            n += 1
        if snew[i+1]=="X":
            n+=1
        output += str(n)
    print (output)


def decode(s):
    nxx=[]
    nx=[]
    n=[]
    output = ""
    for i in range (0,len(s)):
        output += "0"

    for i in range (0,len(s)):
        if s[i]=="2":
            output = output[0:i-1]+"X"+output[i]+"X"+output[i+2:]
        if s[i]=="0":
            output = output[0:i-1]+" "+output[i]+" "+output[i+2:]
    verander1tjes(output,s)
    
def verander1tjes(output,s):
    
    for i in range (0,len(s)):
        if i != 0 and i!= len(s)-1:
            
            if s[i]=="1":
                if output[i-1]=="0" or output[i+1]=="0":
                    if output[i-1]=="x":
                        output = output [0:i+1]+" "+output[i+2:]
                    if output[i+1]=="x":
                        output = output [0:i-1]+" "+output[i:]
                    
                    if output[i-1]==" ":
                        output = output [0:i+1]+"X"+output[i+2:]
                    if output[i+1]==" ":
                        output = output [0:i-1]+"X"+output[i:] 
                    
                    
                if output[i-1]=="0" and output[i+1]=="0":
                    output = output [0:i+1]+"X"+output[i+2:]
                    verander1tjes(output,s)
                    output = output [0:i-1]+"X"+output[i:]
                    verander1tjes(output,s)
    
    print (output)            
                
                
                