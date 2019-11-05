def encode(s, n):
    if len(s)==0:
        print("")
    for i in s:
        if "a"<=i<="z":
            if ord(i)+n > ord("z"):
                i=ord(i)-26
                i = chr(i)
            else:
                i = ord(i)+n 
                i = chr(i)
            print(i,end="")
        else:
            print(i,end="")

def decode(s, n):
    if len(s)==0:
        print("")
    for i in s:
        if "a"<=i<="z":
            if ord(i)+n < ord("a"):
                i=ord(i)-26
                i = chr(i)
            else:
                i = ord(i)+n
                i = chr(i)
            print(i,end="")
        else:
            print(i,end="")