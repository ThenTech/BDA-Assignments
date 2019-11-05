# write your code here
a=int(input("stukken van 1 cent"))
b=int(input("stukken van 2 cent"))
c=int(input("stukken van 5 cent"))
d=int(input("stukken van 10 cent"))
e=int(input("stukken van 20 cent"))

a=(a*0.01)
b=(b*0.02)
c=(c*0.05)
d=(d*0.1)
e=(e*0.2)

euros= int(a+b+c+d+e)
cents= float(a+b+c+d+e) - euros

print("You have " + str(euros) + "." + str(cents) +" euro!")