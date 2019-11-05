oneEurocents = int(input())
twoEurocents = int(input())
fiveEurocents = int(input())
tenEurocents = int(input())
twentyEurocents = int(input())

total = oneEurocents + twoEurocents * 2 + fiveEurocents * 5 + tenEurocents * 10 + twentyEurocents * 20
euros = total // 100
eurocents1 = total % 100 // 10
eurocents2 = total % 10

print("You have ", euros, ".", eurocents1, eurocents2, " euro!", sep="")
