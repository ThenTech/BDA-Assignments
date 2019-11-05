rijen = int(input("Geef een aantal: "))
kolomen = int(input("geeef een aantal: "))
a = rijen * kolomen
b = 1

while b <= a:
    if b%rijen == 0:
        print(b)
        b +=1
    else:
        print(b, end=" ")
        b +=1
