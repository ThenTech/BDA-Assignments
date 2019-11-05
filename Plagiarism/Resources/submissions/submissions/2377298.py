# write your code here
x=int(input("give an integer"))
y=int(input("give an integer"))
total_y=0
total_x=0
product=1
for i in range(y):
    total_y=(y-i)
    total_x =(x-i)
    quotient=float(total_x/total_y)
    product*=quotient
print(int(product))