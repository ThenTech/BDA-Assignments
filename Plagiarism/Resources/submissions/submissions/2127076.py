# write your code here
oneEurocents  = int(input());
twoEurocents = int(input());
fiveEurocents = int(input());
tenEurocents = int(input());
twentyEurocents = int(input());

total = oneEurocents + twoEurocents * 2 + fiveEurocents * 5 + tenEurocents * 10 + twentyEurocents * 20;

print("You have ", total // 100, ".", total % 100, " euro!", sep="")