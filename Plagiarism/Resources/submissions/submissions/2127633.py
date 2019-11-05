total = input()

two: print("2-euros:", (int(total)//200))
resttwo = int(total)%200

one: print("1-euros:", (int(resttwo)//100))
restone = int(resttwo)%100

fiftyc: print("50c-euros:", (int(restone)//50))
restfiftyc = int(restone)%50

twentyc: print("20c-euros:", (int(restfiftyc)//20))
resttwentyc = int(restfiftyc)%20

tenc: print("10c-euros:", (int(resttwentyc)//10))
resttenc = int(resttwentyc)%10

fivec: print("5c-euros:", (int(resttenc)//5))
restfivec = int(resttenc)%5

twoc: print("2c-euros:", (int(restfivec)//2))
resttwoc = int(restfivec)%2

onec: print("1c-euros:", (int(resttwoc)//1))
restonec = int(resttwoc)%1