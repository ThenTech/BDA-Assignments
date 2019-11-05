# write your code here

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
o = 0
p = 0
q = 0
r = 0
s = 0
t = 0
u = 0
v = 0
w = 0
x = 0
y = 0
z = 0
space = 0

sentence = input("input string: ")
value = 0

while value + 1 <= len(sentence):
    if sentence[value] == "a":
        a += 1
    elif sentence[value] == "b":
        b += 1
    elif sentence[value] == "c":
        c += 1
    elif sentence[value] == "d":
        d += 1
    elif sentence[value] == "e":
        e += 1
    elif sentence[value] == "f":
        f += 1
    elif sentence[value] == "g":
        g += 1
    elif sentence[value] == "h":
        h += 1
    elif sentence[value] == "i":
        i += 1
    elif sentence[value] == "j":
        j += 1
    elif sentence[value] == "k":
        k += 1
    elif sentence[value] == "l":
        l += 1
    elif sentence[value] == "m":
        m += 1
    elif sentence[value] == "n":
        n += 1
    elif sentence[value] == "o":
        o += 1
    elif sentence[value] == "p":
        p += 1
    elif sentence[value] == "q":
        q += 1
    elif sentence[value] == "r":
        r += 1
    elif sentence[value] == "s":
        s += 1
    elif sentence[value] == "t":
        t += 1
    elif sentence[value] == "u":
        u += 1
    elif sentence[value] == "v":
        v += 1
    elif sentence[value] == "w":
        w += 1
    elif sentence[value] == "x":
        x += 1
    elif sentence[value] == "y":
        y += 1
    elif sentence[value] == "z":
        z += 1
    elif sentence[value] == " ":
        space += 1
    value += 1
    
a1 = 0
b1 = 0
c1 = 0
d1 = 0
e1 = 0
f1 = 0
g1 = 0
h1 = 0
i1 = 0
j1 = 0
k1 = 0
l1 = 0
m1 = 0
n1 = 0
o1 = 0
p1 = 0
q1 = 0
r1 = 0
s1 = 0
t1 = 0
u1 = 0
v1 = 0
w1 = 0
x1 = 0
y1 = 0
z1 = 0
space1 = 0
    
sentence1 = input("input string: ")
value = 0

while value + 1 <= len(sentence1):
    if sentence1[value] == "a":
        a1 += 1
    elif sentence1[value] == "b":
        b1 += 1
    elif sentence1[value] == "c":
        c1 += 1
    elif sentence1[value] == "d":
        d1 += 1
    elif sentence1[value] == "e":
        e1 += 1
    elif sentence1[value] == "f":
        f1 += 1
    elif sentence1[value] == "g":
        g1 += 1
    elif sentence1[value] == "h":
        h1 += 1
    elif sentence1[value] == "i":
        i1 += 1
    elif sentence1[value] == "j":
        j1 += 1
    elif sentence1[value] == "k":
        k1 += 1
    elif sentence1[value] == "l":
        l1 += 1
    elif sentence1[value] == "m":
        m1 += 1
    elif sentence1[value] == "n":
        n1 += 1
    elif sentence1[value] == "o":
        o1 += 1
    elif sentence1[value] == "p":
        p1 += 1
    elif sentence1[value] == "q":
        q1 += 1
    elif sentence1[value] == "r":
        r1 += 1
    elif sentence1[value] == "s":
        s1 += 1
    elif sentence1[value] == "t":
        t1 += 1
    elif sentence1[value] == "u":
        u1 += 1
    elif sentence1[value] == "v":
        v1 += 1
    elif sentence1[value] == "w":
        w1 += 1
    elif sentence1[value] == "x":
        x1 += 1
    elif sentence1[value] == "y":
        y1 += 1
    elif sentence1[value] == "z":
        z1 += 1
    elif sentence1[value] == " ":
        space1 += 1
    value += 1
    
list2 = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
list1 = [a1, b1, c1, d1, e1, f1, g1, h1, i1, j1, k1, l1, m1, n1, o1, p1, q1, r1, s1, t1, u1, v1, w1, x1, y1, z1]

if list1 == list2:
    print(sentence, "and", sentence1, "are anagrams")
elif list1 != list2:
    print(sentence, "and", sentence1, "are not anagrams")