a = int(input("Give "))
b = int(input("Also ")) 

d = 1
for i in range(b):
    c = (a - i)/(b-i)
    d = d * c
print(int(d))