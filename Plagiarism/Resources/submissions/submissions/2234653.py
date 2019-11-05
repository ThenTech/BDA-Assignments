gdag = input()
gmaand= input()
gjaar = input()
cdag= input()
cmaand = input()
cjaar=input()
leeftijd= int(cjaar)-int(gjaar)
if int(cmaand)-int(gmaand)>=0:
    if int(cdag)-int(gdag)>=0:
        leeftijd=int(leeftijd)+1
print(leeftijd)