onecent = int(input("how many coins of one cent? "))
twocent = int(input("how many coins of two cent? "))
fivecent = int(input("how many coins of five cent? "))
tencent = int(input("how many coins of ten cent? "))
twentycent = int(input("how many coins of twenty cent? "))

totalcent = onecent*1 + twocent*2 + fivecent*5 + tencent*10 + twentycent*20
totaleuro = totalcent*0.01

print("you have ", totaleuro, " euro!", sep="")