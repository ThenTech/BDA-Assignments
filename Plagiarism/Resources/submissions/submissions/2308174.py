inpinp = int(input())

a = inpinp // 200
inp1 = inpinp - a*200
b = inp1 // 100
inp2 = inp1 - b*100
c = inp2 // 50
inp3 = inp2 - c*50
d = inp3 // 20
inp4 = inp3 - d*20
e = inp4 // 10
inp5 = inp4 - e*10
f = inp5 //5
inp6 = inp5 - f*5
g = inp6 //2
inp7 = inp6 - g*2
h = inp7 //1

print("2-euros:", a )
print("1-euros:", b )
print("50c-euros:", c )
print("20c-euros:", d )
print("10c-euros:", e )
print("5c-euros:", f )
print("2c-euros:", g )
print("1c-euros:", h )
