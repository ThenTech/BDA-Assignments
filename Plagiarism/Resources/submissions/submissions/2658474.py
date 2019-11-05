def encode(s, n):
    string =""
    if len(s)==0:
        print(string)
    for i in s:
        if "a"<=i<="z":
            if ord(i)+n > ord("z"):
                i=(ord(i)+n)%26
                i = chr(i)
            else:
                i = ord(i)+n 
                i = chr(i)
            string += i
        else:
            string += i
    return string

def decode(s, n):
    string = ""
    if len(s)==0:
        print("")
    for i in s:
        if "a"<=i<="z":
            if ord(i)+n < ord("a"):
                i=(ord(i)+n)%26
                i = chr(i)
            else:
                i = ord(i)+n
                i = chr(i)
            string += i
        else:
            string += i
    return string