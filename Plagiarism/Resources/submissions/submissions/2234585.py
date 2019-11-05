gdag = input()
gmaand= input()
gjaar = input()
cdag= input()
cmaand : input()
cjaar=input()
leeftijd= cjaar-gjaar
if cmaand-gmaand>=0:
    if cdag-gdag>=0:
        leeftijd=leeftijd+1
print(leeftijd)