dia=int(input("dia: "))
mes=int(input("mes: "))
anho= int(input("anho: "))

hoydia=int(input("hoy dia: "))
meshoy=int(input("mes dia: "))
anhohoy=int(input("anho dia: "))


edad = anhohoy - anho - 1

if (meshoy > mes):
    edad = edad + 1
elif (meshoy== mes and hoydia >= dia):
    edad = edad + 1

print(edad)