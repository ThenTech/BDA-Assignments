dinero = int(input("dinero: "))


moneda2 = dinero // 200
dinero = dinero % 200

moneda1 = dinero // 100
dinero = dinero % 100


moneda50 = dinero // 50
dinero = dinero % 50


moneda20 = dinero // 20
dinero = dinero % 20


moneda10 = dinero // 10
dinero = dinero % 10


moneda5 = dinero // 5
dinero = dinero % 5


monedad2 = dinero // 2
dinero = dinero % 2

print("2-euros:", moneda2)
print("1-euros:", moneda1 )
print("50c-euros:", moneda50)
print("20c-euros:", moneda20)
print("10c-euros:", moneda10)
print("5c-euros:", moneda5)
print("2c-euros:", monedad2)
print("1c-euros:", dinero)

