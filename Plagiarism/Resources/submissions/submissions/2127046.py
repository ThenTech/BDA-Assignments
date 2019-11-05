pay = int(input("how many eurocents to pay? "))

twoEUR      = pay//200
oneEUR      = pay%200//100
fiftyCENT   = pay%200%100//50
twentyCENT  = pay%200%100%50//20
tenCENT     = pay%200%100%50%20//10
fiveCENT    = pay%200%100%50%20%10//5
twoCENT     = pay%200%100%50%20%10%5//2
oneCENT     = pay%200%100%50%20%10%5%2//1

print("2-euros: ",  twoEUR)
print("1-euros: ",  oneEUR)
print("50-cents: ", fiftyCENT)
print("20-cents: ", twentyCENT)
print("10-cents: ", tenCENT)
print("5-cents: ",  fiftyCENT)
print("2-cents: ",  twoCENT)
print("1-cents: ",  oneCENT)