# write your code here
geboortedag= int(input())
geboortemaand = int(input())
geboortejaar=int(input())
currendag=int(input())
currentmaand=int(input())
currentjaar=int(input())
jaren=currentjaar - geboortejaar
if (geboortemaand-currentmaand > 0):
    jaren -=1
elif (geboortemaand - currentmaand == 0 and geboortedag - geboortedag > 0):
    jaren -1
print(jaren)