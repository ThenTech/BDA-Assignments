# write your code here
OneCent = input("How many 1 cents?")
TwoCent = input("How many 2 cents?")
FiveCent = input("How many 5 cents?")
TenCent = input("How many 10 cents?")
TwentyCent = input("How many 20 cents?")

OneCentfloat = float(OneCent)
TwoCentfloat = float(TwoCent)
FiveCentfloat = float(FiveCent)
TenCentfloat = float(TenCent)
TwentyCentfloat = float(TwentyCent)

OneC = OneCentfloat*0.01
TwoC = TwoCentfloat*0.02
FiveC = FiveCentfloat*0.05
TenC = TenCentfloat*0.10
TwentyC = TwentyCentfloat*0.20

sum = OneC+TwoC+FiveC+TenC+TwentyC

print("You have ", "{0:.2f}".format(sum), " euro!", sep="")