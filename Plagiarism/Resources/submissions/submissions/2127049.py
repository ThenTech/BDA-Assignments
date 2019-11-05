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
print("50c-euros: ", fiftyCENT)
print("20c-euros: ", twentyCENT)
print("10c-euros: ", tenCENT)
print("5c-euros: ",  fiftyCENT)
print("2c-euros: ",  twoCENT)
print("1c-euros: ",  oneCENT)