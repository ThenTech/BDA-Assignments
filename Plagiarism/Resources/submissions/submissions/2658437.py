def encode(s, n):
    for i in s:
        if "a"<=i<="z":
            if ord(i)+n > ord("z"):
                i=ord(i)-26
                i = chr(i)
            else:
                i = ord(i)+n ord("z")
                i = chr(i)
            print(i,end="")
        else:
            print(i)

def decode(s, n):
    for i in s:
        if "a"<=i<="z":
            if ord(i)+n < ord("a"):
                i=ord(i)-26
                i = chr(i)
            else:
                i = ord(i)+n ord("a")
                i = chr(i)
            print(i,end="")
        else:
            print(i)