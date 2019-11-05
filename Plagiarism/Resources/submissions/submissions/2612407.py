# write your code here
day = int(input())
month = int(input())
year = int(input())
mDay = int(input())
mMonth = int(input())
mYear = int(input())
output = 0

if (mMonth>= month and mDay>=day):
    ouput = mYear - year
else:  
    output = mYear - year - 1
if output < 0:
    output *= -1
print(output)