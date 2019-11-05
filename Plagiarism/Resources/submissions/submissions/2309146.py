x = int(input())

a = 0
for i in range(1, x+1):  # fout was eerst range(len gebruiken -> gaat niet op int
    a += i

print(a)
