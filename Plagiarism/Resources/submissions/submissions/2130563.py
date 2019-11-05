teller=int(input("Geef teller"))
noemer=int(input("Geef noemer"))
resultaat=1
for i in range(0,(y-1)):
    resultaat=(teller-i)/(noemer-i)*resultaat
    print(resultaat)