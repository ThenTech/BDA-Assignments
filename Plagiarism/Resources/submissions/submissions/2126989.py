onecent = int(input("how many coins of one cent? "))
twocent = int(input("how many coins of two cent? "))
fivecent = int(input("how many coins of five cent? "))
tencent = int(input("how many coins of ten cent? "))
twentycent = int(input("how many coins of twenty cent? "))

totalcent = onecent*1 + twocent*2 + fivecent*5 + tencent*10 + twentycent*20
totaleuro = totalcent//100
totaltens = totalcent%100//10
totalones = totalcent%100%10

print("You have ", totaleuro , ".", totaltens, totalones, " euro!", sep="")