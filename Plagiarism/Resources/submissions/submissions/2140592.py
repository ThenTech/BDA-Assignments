dag = int(input("Op welke dag ben je geboren? "))
maand = int(input("in welke maand ben je geboren? "))
jaar = int(input("in welk jaar ben je geboren? "))

dagVandaag = int(input("welke dag is het vandaag? "))
maandVandaag = int(input("Welke maand is het vandaag? "))
jaarVandaag = int(input("Welk jaar is het vandaag? "))

leeftijd = 0

if jaarVandaag >= jaar:
    leeftijd = jaarVandaag - jaar -1
    if maandVandaag >= maand:
        if dagVandaag >= dag:
            leeftijd += 1
            print(leeftijd)
        else:
            print(leeftijd)
    else:
        print(leeftijd)
else:
    print("De ingegeven leeftijd klopt niet.")