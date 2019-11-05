string = input("Geef zin")
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0
k=0
l=0
m=0
n=0
o=0
p=0
q=0
r=0
s=0
t=0
u=0
v=0
w=0
x=0
y=0
z=0
for plaats in range(len(string)):
    if string[plaats] in letters:
        if string[plaats] == 'a':
            a += 1
        elif string[plaats] == 'b':
            b += 1
        elif string[plaats] == 'c':
            c += 1
        elif string[plaats] == 'd':
            d += 1
        elif string[plaats] == 'e':
            e += 1
        elif string[plaats] == 'f':
            f += 1
        elif string[plaats] == 'g':
            g += 1
        elif string[plaats] == 'h':
            h += 1
        elif string[plaats] == 'i':
            i += 1
        elif string[plaats] == 'j':
            j += 1
        elif string[plaats] == 'k':
            k += 1
        elif string[plaats] == 'l':
            l += 1
        elif string[plaats] == 'm':
            m += 1
        elif string[plaats] == 'n':
            n += 1
        elif string[plaats] == 'o':
            o += 1
        elif string[plaats] == 'p':
            p += 1
        elif string[plaats] == 'q':
            q += 1
        elif string[plaats] == 'r':
            r += 1
        elif string[plaats] == 's':
            s += 1
        elif string[plaats] == 't':
            t += 1
        elif string[plaats] == 'u':
            u += 1
        elif string[plaats] == 'v':
            v += 1
        elif string[plaats] == 'w':
            w += 1
        elif string[plaats] == 'x':
            x += 1
        elif string[plaats] == 'y':
            y += 1
        elif string[plaats] == 'z':
            z += 1
print("a:",a)
print("b:",b)
print("c:",c)
print("d:",d)
print("e:",e)
print("f:",f)
print("g:",g)
print("h:",h)
print("i:",i)
print("j:",j)
print("k:",k)
print("l:",l)
print("m:",m)
print("n:",n)
print("o:",o)
print("p:",p)
print("q:",q)
print("r:",r)
print("s:",s)
print("t:",t)
print("u:",u)
print("v:",v)
print("w:",w)
print("x:",x)
print("y:",y)
print("z:",z)